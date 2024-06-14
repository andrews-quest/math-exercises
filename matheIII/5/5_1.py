import numpy as np
import matplotlib.pyplot as plt

t_vals = [x for x in np.linspace(0, 20, 100)]
x_vals = [0]
y_vals = [0]
x_speed = 1
y_speed = 1


def compute(x_vals, y_vals, t_vals, x_speed, y_speed):
    t_dist = t_vals[1] - t_vals[0]
    for t in t_vals:
        x_acc = (-2/5) * y_vals[-1]
        y_acc = (-3/5) * x_vals[-1]
        x_speed = x_speed + x_acc
        y_speed = y_speed + y_acc
        x_vals.append(y_vals[-1] + x_speed * t_dist)
        y_vals.append(x_vals[-1] + y_speed * t_dist)


def plot(x_vals, y_vals):
    plt.plot(x_vals, y_vals)
    plt.show()


compute(x_vals, y_vals, t_vals, x_speed, y_speed)
plot(x_vals, y_vals)
