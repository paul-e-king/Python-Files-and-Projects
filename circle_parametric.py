import matplotlib.pyplot as plt
import numpy as np

plt.xlim([-5, 5])
plt.ylim([-5, 5])

angle = np.linspace(0, np.pi*2, 150)

# radius = 0.4
radius = 3

x = radius * np.cos(angle)
y = radius * np.sin(angle)

figure, axes = plt.subplots(1)

axes.plot(x, y)
angle = np.linspace(5*np.pi/4, 7*np.pi/4, 150)  # smile
x = 0.75 * radius * np.cos(angle)
y = 0.75 * radius * np.sin(angle)
axes.plot(x, y)
axes.set_aspect(1)

plt.title('Parametric Circle')
plt.show()

