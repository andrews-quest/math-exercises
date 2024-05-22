from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from random import randint
import numpy as np

n = 200
m = 100
y = [randint(0, 20)+0.2*i for i in range(0, round(n/2))]
y.extend([randint(0,20)-0.2*i for i in range(round(n/2), n)])

x = [i for i in np.linspace(0, m, n)]


def func(x, a, b):
    return a*(x**2) + b

fit = curve_fit(func, x, y)

a_fit = fit[0][0]
b_fit = fit[0][1]

curve = []
for i in x:
    curve.append(func(i, a_fit, b_fit))
print(curve)

plt.plot(x, curve)
plt.plot(x, y)
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.show()