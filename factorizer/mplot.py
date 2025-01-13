import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2

x = np.linspace(-5, 5, 1000)
y = f(x)

plt.plot(x, y)
plt.show()
