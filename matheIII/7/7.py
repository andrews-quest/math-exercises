import matplotlib.pyplot as plt
import numpy as np
import manim

x_0 = 3.3

x_vals = np.linspace(0, 4, 100)
polynom_vals = []

def polynom(x):
    return x**5 - 3*x**4 - 4*x**3 + 12*x**2 - 5*x + 15

for x in x_vals:
    polynom_vals.append(polynom(x))

def derivative(x):
    return 5*x**4 - 12*x**3 - 12*x**2 + 24*x - 5

def newton(x_i):
    return x_i - (polynom(x_i))/(derivative(x_i))

def newton2(x_i, x_found):
    return x_i - 1 / (derivative(x_i) / polynom(x_i) - 1 / (x_i - x_found))

def newton3(x_i, x_found, x_found2):
    return newton2(x_i, x_found) - 1 / (x_i - x_found2)

def plot():
    plt.plot(x_vals, polynom_vals)
    plt.show()

for t in range(0, 15):
    x_0 = newton(x_0)
    print(x_0)

print("\nsecond point:\n")

x_found = x_0
x_0 = 3.3
for t in range(0, 15):
    x_0 = newton2(x_0, x_found)
    print(x_0)

print("\nthird point:\n")

x_found2 = x_0
x_0 = 3.3
for t in range(0, 25):
    x_0 = newton3(x_0, x_found, x_found2)
    print(x_0)
