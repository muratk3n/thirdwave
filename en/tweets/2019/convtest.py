import numpy as np
from scipy.optimize import rosen

def _gen_pairs(gen, max_iter, max_inner, random_state, verbose):
    rng = np.random.RandomState(random_state)
    if isinstance(gen, tuple):
        shape = gen
        gen = lambda rng: rng.randn(*shape)

    for it in range(max_iter):
        if verbose:
            print("iter", it + 1)

        M1 = gen(rng)
        M2 = gen(rng)
        for t in np.linspace(0.01, 0.99, max_inner):
            M = t * M1 + (1 - t) * M2
            yield M, M1, M2, t

def check_convex(func, gen, max_iter=1000, max_inner=10,
                 quasi=False, random_state=None, eps=1e-9, verbose=0):
    for M, M1, M2, t in _gen_pairs(gen, max_iter, max_inner,
                                   random_state, verbose):
        if quasi:
            diff = func(M) - max(func(M1), func(M2))
        else:
            diff = func(M) - (t * func(M1) + (1 - t) * func(M2))

        if diff > eps:
            print("not convex (diff=%f)" % diff)
            return
