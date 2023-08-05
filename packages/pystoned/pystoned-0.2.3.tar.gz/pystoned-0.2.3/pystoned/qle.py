"""
@title  : quasi-Likelihood function for residuals (eps) given normal-half normal 
          distribution and parameter lambda
@Author : Sheng Dai, Timo Kuosmanen
@Mail   : sheng.dai@aalto.fi (S. Dai); timo.kuosmanen@aalto.fi (T. Kuosmanen)  
@Date   : 2020-04-12 
"""

import numpy as np
import math
from scipy.stats import norm


def qllf(lamda, eps):
    # sigma2 Eq. (3.26) in Johnson and Kuosmanen (2015)
    sigma2 = np.mean(eps ** 2) / (1 - 2 * lamda ** 2 / (math.pi * (1 + lamda ** 2)))

    # bias adjusted residuals Eq. (3.25)
    # mean
    mu = math.sqrt((2 * lamda ** 2 * sigma2) / (math.pi * (1 + lamda ** 2)))

    # adj. res.
    epsilon = eps - mu

    # log-likelihood function Eq. (3.24)
    pn = norm.cdf(-epsilon * lamda / math.sqrt(sigma2))
    logl = -len(eps) * math.log(math.sqrt(sigma2)) + np.sum(np.log(pn)) - 0.5 * np.sum(epsilon ** 2) / sigma2
    neg_logl = -logl

    return neg_logl