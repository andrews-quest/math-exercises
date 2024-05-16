import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-1, 1, 30)
y_values = np.exp(x_values)
x_points = [-1, 0, 1]
y_points = np.exp(x_points)
h = 1 - (-1)

polynomial_values = []

def teor_error(n=2):
    return str((1/(1+n)) * (h**(n+1)) * ((1/3)**n) * (np.exp(1)))

def polynomial(val):
    a0 = y_points[0]
    a1 = (y_points[1] - y_points[0])/(x_points[1] - x_points[0])
    a2 = (((y_points[2] - y_points[1])/(x_points[2] - x_points[1])) - a1)/(x_points[2] - x_points[0])
    return a0 + a1*(val-x_points[0]) + a2*(val-x_points[0])*(val-x_points[1])

def pract_error():
    maximal_difference = 0
    for i in range(0, len(polynomial_values)):
        if polynomial_values[i] - y_values[i] > maximal_difference:
            maximal_difference = polynomial_values[i] - y_values[i]
    return str(maximal_difference)

for x in x_values:
    polynomial_values.append(polynomial(x))

print("Die teoretisch ausgerechnete Fehler ist " + teor_error())
print("Die tatsächliche maximale Abweichung ist " + pract_error())
plt.plot(x_values, y_values)
plt.plot(x_values, polynomial_values)
plt.show()