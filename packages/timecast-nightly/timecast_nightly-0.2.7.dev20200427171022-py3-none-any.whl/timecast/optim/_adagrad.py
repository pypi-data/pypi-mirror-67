"""timecast.optim._adagrad"""
import flax
import jax.numpy as jnp
import numpy as onp


@flax.struct.dataclass
class _AdagradHyperParams:
    """Adagrad hyper parameters"""

    learning_rate: float
    eps: float


@flax.struct.dataclass
class _AdagradParamState:
    """Adagrad parameter state"""

    G: onp.ndarray


class Adagrad(flax.optim.OptimizerDef):
    """Adagrad optimizer"""

    def __init__(self, learning_rate: float = 1.0, eps=1e-8):
        """Initialize hyper parameters"""
        hyper_params = _AdagradHyperParams(learning_rate, eps)
        super().__init__(hyper_params)

    def init_param_state(self, param):
        """Initialize parameter state"""
        return _AdagradParamState(jnp.zeros_like(param))

    def apply_param_gradient(self, step, hyper_params, param, state, grad):
        """Apply per-parameter gradients"""

        new_G = state.G + jnp.square(grad)
        new_param = param - hyper_params.learning_rate * grad / jnp.sqrt(new_G + hyper_params.eps)
        new_state = _AdagradParamState(new_G)

        return new_param, new_state
