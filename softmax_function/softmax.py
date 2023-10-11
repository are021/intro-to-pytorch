import numpy as np

# Softmax Function for Converting Values into Probabilities

# L - List of numbers
# Return List of values softmax value
def softmax(L):
    total = sum(np.exp(L))
    res = []
    for val in L:
        res.append((np.exp(val) / total))

    return res

# can also just do this
# expList = np.exp(L)
# return np.divide (expList, expList.sum())