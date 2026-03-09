#marckov_and_chebysev_inequality.py

""" Marckov inequality: P(X >= a) <= E(X)/a
    Chebysev inequality: P(|X - E(X)| >= k) <= Var(X)/k^2
"""

import numpy as np
def marckov_inequality(X, a):
    return f"The probability that X is greater than or equal to {a} is {np.mean(X >= a)}"


