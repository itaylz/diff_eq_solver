import numpy as np

def euler(f, y0, t):
    """
    f: function f(t, y)
    y0: initial value
    t: array of time points
    """
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + (t[i] - t[i-1]) * f(t[i-1], y[i-1])
    return y