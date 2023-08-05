"""
Basic PDFs are provided here. Gauss, exponential... that can be used together with Functors to
build larger models.
"""

#  Copyright (c) 2020 zfit

import math as mt

import numpy as np
import tensorflow as tf

from zfit import z
from ..core.basepdf import BasePDF
from ..core.space import Space, ANY_LOWER, ANY_UPPER
from ..util import ztyping
from ..util.exception import AnalyticIntegralNotImplementedError
from ..util.warnings import warn_advanced_feature

infinity = mt.inf


class CustomGaussOLD(BasePDF):

    def __init__(self, mu, sigma, obs, name="Gauss"):
        super().__init__(name=name, obs=obs, params=dict(mu=mu, sigma=sigma))

    def _unnormalized_pdf(self, x):
        x = x.unstack_x()
        mu = self.params['mu']
        sigma = self.params['sigma']
        gauss = tf.exp(- 0.5 * tf.square((x - mu) / sigma))

        return gauss


def _gauss_integral_from_inf_to_inf(limits, params, model):
    return tf.sqrt(2 * z.pi) * params['sigma']


CustomGaussOLD.register_analytic_integral(func=_gauss_integral_from_inf_to_inf,
                                          limits=Space(limits=(-infinity, infinity), axes=(0,)))


class Exponential(BasePDF):
    _N_OBS = 1

    def __init__(self, lambda_, obs: ztyping.ObsTypeInput, name: str = "Exponential",
                 **kwargs):
        """Exponential function exp(lambda * x).

        The function is normalized over a finite range and therefore a pdf. So the PDF is precisely
        defined as :math:`\\frac{ e^{\\lambda \\cdot x}}{ \\int_{lower}^{upper} e^{\\lambda \\cdot x} dx}`

        Args:
            lambda_ (:py:class:`~zfit.Parameter`): Accessed as parameter "lambda".
            obs (:py:class:`~zfit.Space`): The :py:class:`~zfit.Space` the pdf is defined in.
            name (str): Name of the pdf.
            dtype (DType):
        """
        params = {'lambda': lambda_}
        super().__init__(obs, name=name, params=params, **kwargs)
        if not self.space.has_limits:
            warn_advanced_feature("Exponential pdf relies on a shift of the input towards 0 to keep the numerical "
                                  f"stability high. The space {self.space} does not have limits set and no shift"
                                  f" will occure. To set it manually, set _numerics_data_shift to the expected"
                                  f" average values given to this function _in case you want things to be set_."
                                  f"If this sounds unfamiliar, regard this as an error and use a normalization range.",
                                  identifier='exp_shift')
        self._set_numerics_data_shift(self.space)

    def _unnormalized_pdf(self, x):
        lambda_ = self.params['lambda']
        x = x.unstack_x()
        probs = self._numerics_shifted_exp(x=x, lambda_=lambda_)
        tf.debugging.assert_all_finite(probs, f"Exponendial pdf {self} has non valid values. This is likely caused"
                                              f"by numerical problems: if the exponential is too steep, this will"
                                              f"yield NaNs or infs. Make sure that your lambda is small enough and/or"
                                              f" the initial space is in the same"
                                              f" region as your data (and norm_range, if explicitly set differently)."
                                              f" If this issue still persists, please oben an issue on Github:"
                                              f"https://github.com/zfit/zfit")
        return probs  # Don't use exp! will overflow.

    def _numerics_shifted_exp(self, x, lambda_):  # needed due to overflow in exp otherwise, prevents by shift
        return z.exp(lambda_ * (x - self._numerics_data_shift))

    def _set_numerics_data_shift(self, limits):
        lower, upper = [], []
        for limit in limits:
            low, up = limit.rect_limits_np
            lower.append(low)
            upper.append(up)
        lower_val = min(lower)
        upper_val = max(upper)

        value = (upper_val + lower_val) / 2
        value = z.unstable.gather(value, 0, axis=-1)  # removing the last dimension

        # if max(abs(lower_val - value), abs(upper_val - value)) > 710:
        #     warnings.warn(
        #         "Boundaries can be too wide for exponential (assuming lambda ~ 1), expect `inf` in exp(x) and `NaN`s."
        #         "(upper - lower) * lambda should be smaller than 1400 roughly",
        #         category=RuntimeWarning)

        self._numerics_data_shift = value

    # All hooks are needed to set the right shift when "entering" the pdf. The norm range is taken where both are
    # available. No special need needs to be taken for sampling (it samples from the correct region, the limits, and
    # uses the predictions by the `unnormalized_prob` -> that is shifted correctly
    # def _single_hook_integrate(self, limits, norm_range, name='_hook_integrate'):
    #     with self._set_numerics_data_shift(limits=limits):
    #         return super()._single_hook_integrate(limits, norm_range, name)
    #
    # def _single_hook_analytic_integrate(self, limits, norm_range, name="_hook_analytic_integrate"):
    #     with self._set_numerics_data_shift(limits=limits):
    #         return super()._single_hook_analytic_integrate(limits, norm_range, name)
    #
    # def _single_hook_numeric_integrate(self, limits, norm_range, name='_hook_numeric_integrate'):
    #     with self._set_numerics_data_shift(limits=limits):
    #         return super()._single_hook_numeric_integrate(limits, norm_range, name)
    #
    # def _single_hook_partial_integrate(self, x, limits, norm_range, name='_hook_partial_integrate'):
    #     with self._set_numerics_data_shift(limits=limits):
    #         return super()._single_hook_partial_integrate(x, limits, norm_range, name)
    #
    # def _single_hook_partial_analytic_integrate(self, x, limits, norm_range, name='_hook_partial_analytic_integrate'):
    #     with self._set_numerics_data_shift(limits=limits):
    #         return super()._single_hook_partial_analytic_integrate(x, limits, norm_range, name)
    #
    # def _single_hook_partial_numeric_integrate(self, x, limits, norm_range, name='_hook_partial_numeric_integrate'):
    #     with self._set_numerics_data_shift(limits=limits):
    #         return super()._single_hook_partial_numeric_integrate(x, limits, norm_range, name)
    #
    # def _single_hook_normalization(self, limits, name):
    #     with self._set_numerics_data_shift(limits=limits):
    #         return super()._single_hook_normalization(limits, name)
    #
    # # TODO: remove component_norm_range? But needed for integral?
    # def _single_hook_unnormalized_pdf(self, x, name):
    #     if component_norm_range.limits_are_false:
    #         component_norm_range = self.space
    #     if component_norm_range.limits_are_set:
    #         with self._set_numerics_data_shift(limits=component_norm_range):
    #             return super()._single_hook_unnormalized_pdf(x, name)
    #     else:
    #         return super()._single_hook_unnormalized_pdf(x, name)
    #
    # def _single_hook_pdf(self, x, norm_range, name):
    #     with self._set_numerics_data_shift(limits=norm_range):
    #         return super()._single_hook_pdf(x, norm_range, name)
    #
    # def _single_hook_log_pdf(self, x, norm_range, name):
    #     with self._set_numerics_data_shift(limits=norm_range):
    #         return super()._single_hook_log_pdf(x, norm_range, name)
    #
    # def _single_hook_sample(self, n, limits, name):
    #     with self._set_numerics_data_shift(limits=limits):
    #         return super()._single_hook_sample(n, limits, name)


def _exp_integral_from_any_to_any(limits, params, model):
    lambda_ = params['lambda']
    lower, upper = limits.rect_limits_np
    if any(np.isinf([lower, upper])):
        raise AnalyticIntegralNotImplementedError

    integral = _exp_integral_func_shifting(lambd=lambda_, lower=lower, upper=upper, model=model)
    return integral[0]


def _exp_integral_func_shifting(lambd, lower, upper, model):
    def raw_integral(x):
        return model._numerics_shifted_exp(x=x, lambda_=lambd) / lambd  # needed due to overflow in exp otherwise

    lower_int = raw_integral(x=z.constant(lower))
    upper_int = raw_integral(x=z.constant(upper))
    integral = (upper_int - lower_int)
    return integral


# Exponential.register_inverse_analytic_integral()  # TODO: register icdf for exponential


limits = Space(axes=0, limits=(ANY_LOWER, ANY_UPPER))
Exponential.register_analytic_integral(func=_exp_integral_from_any_to_any, limits=limits)
