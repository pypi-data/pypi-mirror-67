import numpy as np
import torch
import torch.distributed as dist
from apex import amp
from mlbench_core.utils.pytorch.distributed import (
    AllReduceAggregation,
    AllReduceAggregationFP16,
)
from mlbench_core.utils.pytorch.distributed import DecentralizedAggregation
from torch.nn.utils import clip_grad_norm_
from torch.optim import Adam, SGD
from torch.optim.optimizer import Optimizer, required
import ctypes

import math
try:
    from apex.optimizers import FusedAdam
except ImportError as e:
    pass

class SparsifiedSGD(Optimizer):
    r"""Implements sparsified version of stochastic gradient descent.

    Args:
        params (iterable): iterable of parameters to optimize or dicts defining
            parameter groups
        lr (float): learning rate
        weight_decay (float, optional): weight decay (L2 penalty) (default: 0)
        sparse_grad_size (int): Size of the sparsified gradients vector (
        default: 10).

    """

    def __init__(self, params, lr=required, weight_decay=0, sparse_grad_size=10):

        if lr is not required and lr < 0.0:
            raise ValueError("Invalid learning rate: {}".format(lr))
        if weight_decay < 0.0:
            raise ValueError("Invalid weight_decay value: {}".format(weight_decay))

        defaults = dict(lr=lr, weight_decay=weight_decay)

        super(SparsifiedSGD, self).__init__(params, defaults)

        self.__create_gradients_memory()
        self.__create_weighted_average_params()

        self.num_coordinates = sparse_grad_size

    def __create_weighted_average_params(self):
        r""" Create a memory to keep the weighted average of parameters in
        each iteration """
        for group in self.param_groups:
            for p in group["params"]:
                param_state = self.state[p]
                param_state["estimated_w"] = torch.zeros_like(p.data)
                p.data.normal_(0, 0.01)
                param_state["estimated_w"].copy_(p.data)

    def __create_gradients_memory(self):
        r""" Create a memory to keep gradients that are not used in each
        iteration """
        for group in self.param_groups:
            for p in group["params"]:
                param_state = self.state[p]
                param_state["memory"] = torch.zeros_like(p.data)

    def step(self, closure=None):
        """Performs a single optimization step.

        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        loss = None
        if closure is not None:
            loss = closure()

        for group in self.param_groups:

            weight_decay = group["weight_decay"]

            for p in group["params"]:

                if p.grad is None:
                    continue
                d_p = p.grad.data

                if weight_decay != 0:
                    d_p.add_(weight_decay, p.data)
                p.data.add_(-d_p)

        return loss

    def sparsify_gradients(self, param, lr):
        """ Calls one of the sparsification functions (random or blockwise)

        Args:
            random_sparse (bool): Indicates the way we want to make the
            gradients sparse
                (random or blockwise) (default: False)
            param (:obj: `torch.nn.Parameter`): Model parameter
        """
        if self.random_sparse:
            return self._random_sparsify(param, lr)
        else:
            return self._block_sparsify(param, lr)

    def _random_sparsify(self, param, lr):
        """ Sparsify the gradients vector by selecting 'k' of them randomly.

        Args:
            param (:obj: `torch.nn.Parameter`): Model parameter
            lr (float): Learning rate

        """

        self.state[param]["memory"] += param.grad.data * lr

        indices = np.random.choice(
            param.data.size()[1], self.num_coordinates, replace=False
        )
        sparse_tensor = torch.zeros(2, self.num_coordinates)

        for i, random_index in enumerate(indices):
            sparse_tensor[1, i] = self.state[param]["memory"][0, random_index]
            self.state[param]["memory"][0, random_index] = 0
        sparse_tensor[0, :] = torch.tensor(indices)

        return sparse_tensor

    def _block_sparsify(self, param, lr):
        """ Sparsify the gradients vector by selecting a block of them.

        Args:
            param (:obj: `torch.nn.Parameter`): Model parameter
            lr (float): Learning rate
        """

        self.state[param]["memory"] += param.grad.data * lr

        num_block = int(param.data.size()[1] / self.num_coordinates)

        current_block = np.random.randint(0, num_block)
        begin_index = current_block * self.num_coordinates

        end_index = begin_index + self.num_coordinates - 1
        output_size = 1 + end_index - begin_index + 1

        sparse_tensor = torch.zeros(1, output_size)
        sparse_tensor[0, 0] = begin_index
        sparse_tensor[0, 1:] = self.state[param]["memory"][
            0, begin_index : end_index + 1
        ]
        self.state[param]["memory"][0, begin_index : end_index + 1] = 0

        return sparse_tensor

    def update_estimated_weights(self, iteration, sparse_vector_size):
        """ Updates the estimated parameters

        Args:
            iteration (int): Current global iteration
            sparse_vector_size (int): Size of the sparse gradients vector
        """
        t = iteration
        for group in self.param_groups:
            for param in group["params"]:
                tau = param.data.size()[1] / sparse_vector_size
                rho = (
                    6
                    * ((t + tau) ** 2)
                    / ((1 + t) * (6 * (tau ** 2) + t + 6 * tau * t + 2 * (t ** 2)))
                )
                self.state[param]["estimated_w"] = (
                    self.state[param]["estimated_w"] * (1 - rho) + param.data * rho
                )

    def get_estimated_weights(self):
        """ Returns the weighted average parameter tensor """
        estimated_params = []
        for group in self.param_groups:
            for param in group["params"]:
                estimated_params.append(self.state[param]["estimated_w"])
        return estimated_params


class CentralizedSparsifiedSGD(SparsifiedSGD):
    r"""Implements centralized sparsified version of stochastic gradient
    descent.

    Args:
        params (iterable): iterable of parameters to optimize or dicts defining
            parameter groups
        lr (float): Learning rate
        weight_decay (float, optional): weight decay (L2 penalty) (default: 0)
        sparse_grad_size (int): Size of the sparsified gradients vector (
        default: 10)
        random_sparse (bool): Whether select random sparsification (default:
        `False`)
        average_models (bool): Whether to average models together (default:
        `True`)

    """

    def __init__(
        self,
        params=None,
        lr=required,
        weight_decay=0,
        sparse_grad_size=10,
        random_sparse=False,
        average_models=True,
    ):
        if not params:
            raise ValueError('"params" not set for optimizer')
        self.average_models = average_models
        self.world_size = dist.get_world_size()
        self.random_sparse = random_sparse
        super(CentralizedSparsifiedSGD, self).__init__(
            params, lr, weight_decay, sparse_grad_size
        )

    def step(self, closure=None):
        """ Aggregates the gradients and performs a single optimization step.

            Arguments:
                closure (callable, optional): A closure that reevaluates the
                model and returns the loss.
        """

        loss = None

        if closure is not None:
            loss = closure()

        for group in self.param_groups:

            weight_decay = group["weight_decay"]
            lr = group["lr"]

            for p in group["params"]:
                # Sparsify the gradients
                sparse_tensor = self.sparsify_gradients(p, lr)
                # Aggregate the gradients
                gathered_list = [
                    torch.zeros_like(sparse_tensor) for _ in range(self.world_size)
                ]
                dist.all_gather(gathered_list, sparse_tensor)
                p.grad.data = torch.zeros_like(p.grad.data)

                if self.random_sparse:
                    for grad_tensor in gathered_list:
                        for index in range(grad_tensor.size()[1]):
                            p.grad.data[0, int(grad_tensor[0, index])] += grad_tensor[
                                1, index
                            ]
                else:
                    for grad_tensor in gathered_list:
                        tensor_size = grad_tensor.size()[1]
                        begin = int(grad_tensor[0, 0])
                        p.grad.data[
                            0, begin : (begin + tensor_size - 1)
                        ] += grad_tensor[0, 1:]

                if self.average_models:
                    p.grad.data /= self.world_size

                if p.grad is None:
                    continue
                d_p = p.grad.data

                if weight_decay != 0:
                    d_p.add_(weight_decay, p.data)
                p.data.add_(-d_p)

        return loss


class DecentralizedSGD(SGD):
    r"""Implements decentralized stochastic gradient descent (optionally
    with momentum).

    Args:
        rank (int): rank of current process in the network
        neighbors (list): list of ranks of the neighbors of current process
        model (:obj:`nn.Module`): model which contains parameters for SGD
        lr (float): learning rate
        momentum (float, optional): momentum factor (default: 0)
        weight_decay (float, optional): weight decay (L2 penalty) (default: 0)
        dampening (float, optional): dampening for momentum (default: 0)
        nesterov (bool, optional): enables Nesterov momentum (default: False)
        average_models (bool): Whether to average models together. (default: `True`)
        use_cuda (bool): Whether to use cuda tensors for aggregation
        by_layer (bool): Aggregate by layer instead of all layers at once
    """

    def __init__(
        self,
        rank=None,
        neighbors=None,
        model=None,
        lr=required,
        momentum=0,
        dampening=0,
        weight_decay=0,
        nesterov=False,
        average_models=True,
        use_cuda=False,
        by_layer=False,
    ):
        if not rank:
            raise ValueError('"rank" not set for optimizer')
        if not neighbors:
            raise ValueError('"neighbors" not set for optimizer')
        if not model:
            raise ValueError('"model" not set for optimizer')
        super(DecentralizedSGD, self).__init__(
            model.parameters(), lr, momentum, dampening, weight_decay, nesterov
        )

        if average_models:
            self.agg_mode = "avg"
        else:
            raise NotImplementedError("Only average model is supported right now.")

        self.model = model
        self.agg = DecentralizedAggregation(
            rank, neighbors, use_cuda=use_cuda
        ).agg_model(by_layer=by_layer)

    def step(self, closure=None):
        """ Aggregates the gradients and performs a single optimization step.

        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        loss = super(DecentralizedSGD, self).step(closure=closure)
        # Averaging the model after updating the gradient separately.
        self.agg(self.model, self.agg_mode)
        return loss


class CentralizedSGD(SGD):
    r"""Implements centralized stochastic gradient descent (optionally with
    momentum).

    Args:
        world_size (int): Size of the network
        model (:obj:`nn.Module`): Model which contains parameters for SGD
        lr (float): learning rate
        momentum (float, optional): momentum factor (default: 0)
        weight_decay (float, optional): weight decay (L2 penalty) (default: 0)
        dampening (float, optional): dampening for momentum (default: 0)
        nesterov (bool, optional): enables Nesterov momentum (default: False)
        average_models (bool): Whether to average models together. (default: `True`)
        use_cuda (bool): Whether to use cuda tensors for aggregation
        by_layer (bool): Aggregate by layer instead of all layers at once
    """

    def __init__(
        self,
        world_size=None,
        model=None,
        lr=required,
        momentum=0,
        dampening=0,
        weight_decay=0,
        nesterov=False,
        average_models=True,
        use_cuda=False,
        by_layer=False,
    ):
        if not world_size:
            raise ValueError('"world_size" not set for optimizer')
        if not model:
            raise ValueError('"model" not set for optimizer')
        super(CentralizedSGD, self).__init__(
            model.parameters(), lr, momentum, dampening, weight_decay, nesterov
        )
        if average_models:
            self.agg_mode = "avg"
        else:
            raise NotImplementedError("Only average model is supported right now.")

        self.model = model
        self.agg = AllReduceAggregation(
            world_size=world_size, use_cuda=use_cuda
        ).agg_grad(by_layer=by_layer)

    def step(self, closure=None):
        """ Aggregates the gradients and performs a single optimization step.

        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        self.agg(self.model, self.agg_mode)
        loss = super(CentralizedSGD, self).step(closure=closure)
        return loss


class SignSGD(SGD):
    r"""Implements sign stochastic gradient descent (optionally with momentum).

    Args:
        params (iterable): iterable of parameters to optimize or dicts defining
            parameter groups
        lr (float): learning rate
        momentum (float, optional): momentum factor (default: 0)
        weight_decay (float, optional): weight decay (L2 penalty) (default: 0)
        dampening (float, optional): dampening for momentum (default: 0)
        nesterov (bool, optional): enables Nesterov momentum (default: False)
        average_models (bool): Whether to average models together. (default:
        `True`)

    """

    def step(self, closure=None):
        """ Aggregates the gradients and performs a single optimization step.

        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        loss = None
        if closure is not None:
            loss = closure()

        for group in self.param_groups:
            weight_decay = group["weight_decay"]
            momentum = group["momentum"]
            dampening = group["dampening"]
            nesterov = group["nesterov"]

            for p in group["params"]:
                if p.grad is None:
                    continue
                d_p = p.grad.data
                if weight_decay != 0:
                    d_p.add_(weight_decay, p.data)
                if momentum != 0:
                    param_state = self.state[p]
                    if "momentum_buffer" not in param_state:
                        buf = param_state["momentum_buffer"] = torch.zeros_like(p.data)
                        buf.mul_(momentum).add_(d_p)
                    else:
                        buf = param_state["momentum_buffer"]
                        buf.mul_(momentum).add_(1 - dampening, d_p)
                    if nesterov:
                        d_p = d_p.add(momentum, buf)
                    else:
                        d_p = buf

                # Update with the sign
                p.data.add_(-group["lr"], torch.sign(d_p))

        return loss


class CentralizedAdam(Adam):
    r"""Implements centralized Adam algorithm.

    Args:
        world_size (int): Size of the network
        model (:obj:`nn.Module`): Model which contains parameters for Adam
        lr (float, optional): learning rate (default: 1e-3)
        betas (Tuple[float, float], optional): coefficients used for computing
            running averages of gradient and its square (default: (0.9, 0.999))
        eps (float, optional): term added to the denominator to improve
            numerical stability (default: 1e-8)
        weight_decay (float, optional): weight decay (L2 penalty) (default: 0)
        amsgrad (boolean, optional): whether to use the AMSGrad variant of this
            algorithm from the paper `On the Convergence of Adam and Beyond`_
            (default: False)
        average_models (bool): Whether to average models together. (default: `True`)
        use_cuda (bool): Whether to use cuda tensors for aggregation
        by_layer (bool): Aggregate by layer instead of all layers at once
    """

    def __init__(
        self,
        world_size=None,
        model=None,
        lr=1e-3,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=0,
        amsgrad=False,
        average_models=True,
        use_cuda=False,
        by_layer=False,
    ):
        if not world_size:
            raise ValueError('"world_size" not set for optimizer')
        if not model:
            raise ValueError('"model" not set for optimizer')
        super(CentralizedAdam, self).__init__(
            model.parameters(), lr, betas, eps, weight_decay, amsgrad
        )
        if average_models:
            self.agg_mode = "avg"
        else:
            raise NotImplementedError("Only average model is supported right now.")

        self.model = model
        self.agg = AllReduceAggregation(
            world_size=world_size, use_cuda=use_cuda
        ).agg_grad(by_layer=by_layer)

    def step(self, closure=None):
        """ Aggregates the gradients and performs a single optimization step.

        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        self.agg(self.model, self.agg_mode)
        loss = super(CentralizedAdam, self).step(closure=closure)
        return loss


lib = ctypes.cdll.LoadLibrary(None)
lib.THCudaHalfTensor_normall.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.THCudaHalfTensor_normall.restype = ctypes.c_float


def fused_norm(input):
    if input.type() == "torch.cuda.HalfTensor":
        # 16384 is half 2 if you stare at it long enough
        return lib.THCudaHalfTensor_normall(
            torch.cuda._state_cdata, input._cdata, 16384
        )
    else:
        return input.norm()


class FP16Optimizer:
    """
    Mixed precision optimizer with dynamic loss scaling and backoff.
    https://docs.nvidia.com/deeplearning/sdk/mixed-precision-training/index.html#scalefactor
    """

    def __init__(
        self,
        fp16_model,
        grad_clip=float("inf"),
        loss_scale=1024,
        dls_downscale=2,
        dls_upscale=2,
        dls_upscale_interval=128,
    ):
        """
        Constructor for the Fp16Optimizer.

        :param fp16_model: model (previously casted to half)
        :param grad_clip: coefficient for gradient clipping, max L2 norm of the
            gradients
        :param loss_scale: initial loss scale
        :param dls_downscale: loss downscale factor, loss scale is divided by
            this factor when NaN/INF occurs in the gradients
        :param dls_upscale: loss upscale factor, loss scale is multiplied by
            this factor if previous dls_upscale_interval batches finished
            successfully
        :param dls_upscale_interval: interval for loss scale upscaling
        """
        self.fp16_model = fp16_model
        self.fp16_params, self.fp32_params = self.initialize_flat_fp32_weight()
        self.since_last_invalid = 0
        self.loss_scale = loss_scale
        self.dls_downscale = dls_downscale
        self.dls_upscale = dls_upscale
        self.dls_upscale_interval = dls_upscale_interval
        self.grad_clip = grad_clip
        self.world_size = dist.get_world_size()

        self.optimizer = None

    def set_optimizer(self, optimizer):
        self.optimizer = optimizer

    # Flattening master weight
    def initialize_flat_fp32_weight(self):
        # Set all gradients to None
        for p in self.fp16_model.parameters():
            p.grad = None

        # Count number of parameters per layer
        nelem = 0
        for p in self.fp16_model.parameters():
            nelem += p.numel()
        fp32_params = torch.empty(nelem, dtype=torch.float32)
        fp16_params = torch.empty(nelem, dtype=torch.float16)

        pointer = 0
        for p in self.fp16_model.parameters():
            nelem = p.numel()
            fp32_params[pointer : pointer + nelem].copy_(p.data.view(-1))
            fp16_params[pointer : pointer + nelem].copy_(p.data.view(-1))
            pointer += nelem

        fp32_params = torch.nn.Parameter(fp32_params, requires_grad=True)
        fp32_params.grad = torch.autograd.Variable(
            fp32_params.data.new(*fp32_params.size())
        )

        fp16_params = torch.nn.Parameter(fp16_params, requires_grad=True)
        fp16_params.grad = torch.autograd.Variable(
            fp16_params.data.new(*fp16_params.size())
        )

        return fp16_params, fp32_params

    @staticmethod
    def fp16_to_fp32_flat_grad(fp32_params, fp16_model):
        pointer = 0
        for p in fp16_model.parameters():
            nelem = p.numel()
            fp32_params.grad.data[pointer : pointer + nelem].copy_(p.grad.data.view(-1))
            pointer += nelem

    @staticmethod
    def fp16_to_fp16_flat_grad(fp16_params, fp16_model):
        fp16_params.grad.data = torch.cat(
            [p.grad.data.view(-1) for p in fp16_model.parameters()]
        )

    @staticmethod
    def fp32_to_fp16_grads(fp16_model, fp32_params):
        pointer = 0
        for p in fp16_model.parameters():
            nelem = p.numel()
            p.data.view(-1).copy_(fp32_params.data[pointer : pointer + nelem])
            pointer += nelem

    def backward_loss(self, loss):
        loss *= self.loss_scale
        loss.backward()

    def step(self, closure=None):
        """
        Performs one step of the optimizer.
        Applies loss scaling, computes gradients in fp16, converts gradients to
        fp32, inverts scaling and applies optional gradient norm clipping.
        If gradients are finite, it applies update to fp32 master weights and
        copies updated parameters to fp16 model for the next iteration. If
        gradients are not finite, it skips the batch and adjusts scaling factor
        for the next iteration.

        :param loss: value of loss function
        :param optimizer: optimizer
        :param update: if True executes weight update
        """

        scaling_factor = self.loss_scale

        # Fused adam optim
        if isinstance(self.optimizer, FusedAdam):
            if self.world_size != 1 and self.fp16_model.retain_allreduce_buffers:
                assert len(self.fp16_model.allreduce_buffers) == 1
                self.fp16_params.grad.data = self.fp16_model.allreduce_buffers[0]

                # Average the all-reduced gradients by world size if APEX
                # doesn't do that
                if not self.fp16_model.gradient_average:
                    scaling_factor *= self.world_size
            else:
                self.fp16_to_fp16_flat_grad(self.fp16_params, self.fp16_model)

            norm = fused_norm(self.fp16_params.grad.data) / scaling_factor
        else:
            self.fp16_to_fp32_flat_grad(self.fp32_params, self.fp16_model)
            if scaling_factor != 1.0:
                self.fp32_params.grad.data /= scaling_factor

            norm = clip_grad_norm_([self.fp32_params], self.grad_clip)

        if math.isfinite(norm):
            if isinstance(self.optimizer, FusedAdam):
                clip_coef = self.grad_clip / (norm + 1e-6)
                if clip_coef >= 1:
                    clip_coef = scaling_factor
                else:
                    clip_coef = scaling_factor / clip_coef
                self.optimizer.step(grads=[self.fp16_params.grad], scale=clip_coef)
            else:
                self.optimizer.step(closure=closure)
            self.fp32_to_fp16_grads(self.fp16_model, self.fp32_params)
            self.since_last_invalid += 1
        else:
            self.loss_scale /= self.dls_downscale
            self.since_last_invalid = 0

        if self.since_last_invalid >= self.dls_upscale_interval:
            self.loss_scale *= self.dls_upscale
            self.loss_scale = min(self.loss_scale, 8192.0)
            self.since_last_invalid = 0

        for p in self.fp16_model.parameters():
            p.grad = None

    def zero_grad(self):
        self.optimizer.zero_grad()


class FP32Optimizer:
    """
    Standard optimizer, computes backward and applies weight update.
    """

    def __init__(self, model, grad_clip=None):
        """
        Constructor for the Fp32Optimizer

        Args:
            model (torch.nn.Module): Model
            grad_clip (float): Coefficient for gradient clipping (max L2 norm of gradients)
        """
        self.model = model
        self.grad_clip = grad_clip
        self.optimizer = None

    def set_optimizer(self, optimizer):
        self.optimizer = optimizer

    def step(self, closure=None):
        """
        Performs one step of the optimizer.
        """
        if self.grad_clip != float("inf"):
            clip_grad_norm_(self.model.parameters(), self.grad_clip)

        loss = self.optimizer.step(closure=closure)
        return loss

    def backward_loss(self, loss):
        loss.backward()

    def zero_grad(self):
        self.optimizer.zero_grad()


class AMPOptimizer:
    """
    Optimizer compatible with AMP.
    Uses AMP to apply loss scaling, computes backward and applies weight
    update.
    """

    def __init__(
        self,
        model,
        optimizer,
        grad_clip=None,
        loss_scale=8192,
        dls_upscale_interval=128,
        average_models=True,
        world_size=1,
        use_cuda=False,
        by_layer=False,
        use_horovod=False,
    ):
        """
        Constructor for the AMPOptimizer

        Args:
            model (torch.nn.Module): Model
            optimizer (torch.optim.optimizer.Optimizer): The underlying optimizer
            grad_clip (float): Coefficient for gradient clipping, max L2 norm of the gradients
            loss_scale:
            dls_upscale_interval:
        """
        self.model = model
        self.grad_clip = grad_clip
        self.optimizer = optimizer
        loss_scaler = amp._amp_state.loss_scalers[0]
        loss_scaler._loss_scale = loss_scale
        loss_scaler._scale_seq_len = dls_upscale_interval

        if average_models:
            self.agg_mode = "avg"
        else:
            raise NotImplementedError("Only average model is supported right now.")

        if use_horovod:
            self.agg = AllReduceAggregationFP16(
                world_size=world_size, use_cuda=use_cuda
            ).agg_grad(by_layer=by_layer)
        else:
            self.agg = AllReduceAggregation(
                world_size=world_size, use_cuda=use_cuda
            ).agg_grad(by_layer=by_layer)

    def backward_loss(self, loss):
        with amp.scale_loss(loss, self.optimizer) as scaled_loss:
            scaled_loss.backward()

    def step(self, closure=None):
        """
        Performs one step of the optimizer.
        """
        if self.grad_clip != float("inf"):
            clip_grad_norm_(amp.master_params(self.optimizer), self.grad_clip)

        self.agg(self.model, self.agg_mode)
        loss = self.optimizer.step(closure=closure)
        return loss

    def zero_grad(self):
        self.optimizer.zero_grad()


optimizers = {
    "centralized_sparsified_sgd": CentralizedSparsifiedSGD,
    "decentralized_sgd": DecentralizedSGD,
    "centralized_sgd": CentralizedSGD,
    "sign_sgd": SignSGD,
    "centralized_adam": CentralizedAdam,
}


def get_optimizer(optimizer, **kwargs):
    r"""Returns an object of the class specified with the argument `optimizer`.

        Args:
            optimizer (str): name of the optimizer
            **kwargs (dict, optional): additional optimizer-specific parameters. For the list of supported parameters
                for each optimizer, please look at its documentation.
        """
    return optimizers[optimizer](**kwargs)
