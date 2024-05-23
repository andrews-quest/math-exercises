from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from random import randint
import numpy as np


def curve(x):
    return (3+(x**2))*(np.e**(2*x))

n = 200
m = 0.5
x = [i for i in np.linspace(0, m, n)]
y = [curve(i) for i in x]




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
plt.show()