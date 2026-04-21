import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    pass
    x = np.asarray(x)
    return 1 / (1 + np.exp(-x))