"""flax.nn.Module for a principal component regression online learner."""
from typing import Any
from typing import Iterable
from typing import Tuple
from typing import Union

import flax
import jax.numpy as jnp
import numpy as onp

from timecast.learners._ar import _ar_gram
from timecast.learners._ar import _compute_kernel_bias_gram
from timecast.learners.base import FitMixin
from timecast.learners.base import NewMixin
from timecast.utils import random


def _compute_pca_projection(X: onp.ndarray, k: int, center=False) -> onp.ndarray:
    """Compute PCA projection"""

    if center:
        X = X - X.mean(axis=0)
        # X /= X.shape[0] - 1

    # Compute SVD
    # X: (steps - history_len + 1, history_len * input_dim) -> (H, d)
    # U: (H, H), but because full_matrices=False, (H, d)
    # S: (min(H, d),)
    # VT: (d, d)
    U, S, VT = jnp.linalg.svd(X, full_matrices=False, compute_uv=True)

    # Get index of top K eigen values
    top_k = (-jnp.square(S)).argsort()[:k]

    # Get projection
    # projection: (d, k)
    projection = VT[top_k].T

    return projection


class PCR(NewMixin, FitMixin, flax.nn.Module):
    """PCR online learner"""

    def apply(
        self,
        x: onp.ndarray,
        history_len: int,
        projection: onp.ndarray,
        output_dim: Union[Tuple[int, ...], int] = 1,
        history: onp.ndarray = None,
        loc: Union[onp.ndarray, float] = None,
        scale: Union[onp.ndarray, float] = None,
    ):
        """
        Todo:
            * AR doesn't take any history
        output_dim (Union[Tuple[int, ...], int]): int or tuple describing
        output shape

        Note:
            * We expect that `x` is one- or two-dimensional
            * We reshape `x` to ensure its first axis is time and its second
              axis is input_features

        Args:
            x (onp.ndarray): input data
            history_len (int): length of AR history length
            output_dim (Union[Tuple[int, ...], int]): int or tuple
            describing output shape
            history (onp.ndarray, optional): Defaults to None. Optional
            initialization for history
            loc: mean for centering data
            scale: std for normalizing data

        Returns:
            onp.ndarray: result
        """
        if jnp.isscalar(x):
            x = jnp.array([[x]])
        if x.ndim == 1:
            x = x.reshape(1, -1)

        self.history = self.state(
            "history", shape=(history_len, x.shape[1]), initializer=flax.nn.initializers.zeros
        )

        if self.is_initializing() and history is not None:
            self.history.value = jnp.vstack((self.history.value, history))[history.shape[0] :]
        elif not self.is_initializing():
            self.history.value = jnp.vstack((self.history.value, x))[x.shape[0] :]

        inputs = self.history.value.reshape(1, -1)

        if loc is not None:
            inputs -= loc

        if scale is not None:
            inputs /= scale

        inputs @= projection

        y = flax.nn.DenseGeneral(
            inputs=inputs,
            features=output_dim,
            axis=(0, 1),
            batch_dims=(),
            bias=True,
            dtype=jnp.float32,
            kernel_init=flax.nn.initializers.zeros,
            bias_init=flax.nn.initializers.zeros,
            precision=None,
            name="linear",
        )
        return y

    @classmethod
    def fit(
        cls,
        data: Iterable[Tuple[onp.ndarray, onp.ndarray, Any]],
        input_dim: int,
        history_len: int,
        output_dim: int = 1,
        k: int = None,
        normalize: bool = True,
        alpha: float = 0.0,
        key: jnp.ndarray = None,
        name: str = "pcr",
        **kwargs
    ) -> flax.nn.Model:
        """Receives data as an iterable of tuples containing input time series,
        true time series

        Todo:
            * We assume input_dim is one-dimensional; we should flatten if not
            * We assume output_feature is 1, but this may not always be true
            * output_dim defaults to 1 and is ignored for now
            * Really intended for passing in timeseries at a time, not
            individual time series observations; is this the right general API?
            * Shape is (1, input_dim); what about mini-batches?

        Notes:
            * Use (1, history_len * input_dim) vectors as features (could
            consider other representations)
            * Ignore true value (i.e., look at features only) (should we
            consider impact of features on dependent variable?)
            * Given a time series of length N and a history of length H,
            construct N - H + 1 windows
            * We could infer input_dim from data, but for now, require
            users to explicitly provide
            * Assumes we get tuples of time series, not individual time series
            observations

        Args:
            data: an iterable of tuples containing input/truth pairs of time
            series plus any auxiliary value
            input_dim: number of feature dimensions in input
            history_len: length of history to consider
            output_dim: number of feature dimensions in output
            k: number of PCA components to keep. Default is min(num_histories,
            normalize: zscore data or not
            input_dim)
            alpha: Parameter to pass to ridge regression for AR fit
            key: random key for jax random
            name: name for the top-level module
            kwargs: Extra keyword arguments

        Returns:
            flax.nn.Model: initialized model
        """
        XTX, XTY = _ar_gram(data, input_dim, output_dim, history_len)
        num_features = input_dim * history_len

        # Compute k
        min_dim = min(num_features, XTX.observations)
        k = min_dim if k is None else min(k, min_dim)

        projection = _compute_pca_projection(XTX.matrix(normalize=normalize), k)

        # X: (n, d)
        # XTX.matrix: (d, d)
        # projection: (d, k)
        # X @ projection: (n, k)
        # (X @ projection).T @ (X @ projection): (k, k)
        # projection.T @ X.T @ X @ projection = (k, d) @ (d, n) @ (n, d) @ (d, k)
        kernel, bias = _compute_kernel_bias_gram(
            XTX.matrix(normalize=normalize, projection=projection, fit_intercept=True),
            XTY.matrix(normalize=normalize, projection=projection, fit_intercept=True),
            alpha=alpha,
        )
        kernel = kernel.reshape(1, k, 1)

        loc = XTX.mean if normalize else None
        scale = XTX.std if normalize else None

        model_def = PCR.partial(
            history_len=history_len,
            projection=projection,
            output_dim=output_dim,
            loc=loc,
            scale=scale,
            name=name,
        )

        if key is None:
            key = random.generate_key()

        with flax.nn.stateful() as state:
            _, params = model_def.init_by_shape(key, [(1, input_dim)])

        model = flax.nn.Model(model_def, params)
        model.params["linear"]["kernel"] = kernel
        model.params["linear"]["bias"] = bias

        return model, state
