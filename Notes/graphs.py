import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x < 0:
        return 0
    elif x > 1:
        return 1
    else:
        return np.exp(-1 / (np.exp(x / (1 - x)) - 1))

def h(ep, x):
    return f(x/ep)

def g(I, ep, x):
    a, b = I 

    if x <= a + ep:
        return h(ep, x - a - ep)
    elif x >= b:
        return h(ep, b - x)
    else: 
        return 1

I = (-1, 1)
ep_space = np.linspace(1e-1, 1e-4)

for ep in ep_space:
    x = np.linspace(I[0] - 1, I[1] + 1, 1000)
    y = np.array([g(I, ep, n) for n in x])
    plt.plot(x, y)

plt.xlabel(r'$x$')
plt.ylabel(r'$\rho(x)$')
plt.title(r'Graph of $\rho(x)$')
plt.grid(True)
plt.legend()
plt.show()