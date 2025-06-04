import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

area_real =  0
area_trapez = 0
area_kepler = 0

sum_dev_kepler = 0
sum_dev_trapez = 0

def deviation_kepler(h, x):
    return (h**5) / 90 * abs(80 * (np.e**(2*x)))

def deviation_trapez(h, x):
    return (h**3) / 12 * abs(20 * np.e**(2*x))


def func(x):
    return np.float64(((x**2) + 3)*(np.e ** (2*x)))

def area_real_func(x):
    return (1/4) * (2*(x**2)-2*x+7)*(np.e**(2*x)) - 7/4

trapez_vals = []
x_trapez_vals = []

def trapez(t, n):
    global x_trapez_vals
    global area_trapez
    global sum_dev_trapez

    x_trapez_vals = [x_n for x_n in np.linspace(0, t, n)]
    y_prev = 0
    h = x_trapez_vals[1]
    for x_n in x_trapez_vals:
        trapez_vals.append(func(x_n))
        area_trapez += (h/2)*(func(x_n) + y_prev)
        y_prev = func(x_n)
        sum_dev_trapez += deviation_trapez(h, x_n)

kepler_vals = []
x_kepler_vals = []
x_kepler_vals_curve = []

def parabola(x, a, b):
    return a*(x**2) + b

def kepler(t, n):
    global x_kepler_vals
    global kepler_vals
    global area_kepler
    global x_kepler_vals_curve
    global sum_dev_kepler

    carry = n%2
    if(carry > 0):
        n += carry

    x_kepler_vals= [x_n for x_n in np.linspace(0, t, n)]
    h = x_kepler_vals[1] - x_kepler_vals[0]
    for i in range(0, n, 2):
        area_kepler += np.float64((h/3)*(func(x_kepler_vals[i]) +
                                            (func((x_kepler_vals[i+1] + x_kepler_vals[i])/2) * 4) +
                                            func(x_kepler_vals[i+1])))

        constants = curve_fit(parabola, [x for x in np.linspace(x_kepler_vals[i], x_kepler_vals[i+1], 100)],
                    [func(x) for x in np.linspace(x_kepler_vals[i], x_kepler_vals[i+1], 100)])

        a_fit = constants[0][0]
        b_fit = constants[0][1]
        x_kepler_vals_curve.extend([x for x in np.linspace(x_kepler_vals[i], x_kepler_vals[i+1], 100)])
        kepler_vals.extend([parabola(x, a_fit, b_fit) for x in np.linspace(x_kepler_vals[i], x_kepler_vals[i+1], 100)])

        sum_dev_kepler += deviation_kepler(h, x_kepler_vals[i+1])


def interpolation(t, n):
    global area_real
    global area_trapez
    global area_kepler
    global sum_dev_kepler
    global sum_dev_trapez

    area_real = area_real_func(t)
    trapez(t, n)
    kepler(t, n)
    print_result()

    # plot(t, n)
    area_kepler = 0
    area_trapez = 0
    sum_dev_kepler = 0
    sum_dev_trapez = 0


def print_result():
    print(f"Die Fläche unter dem Graph beträgt {round(area_real, 2)}")
    print(f"Die Fläche nach der Trapezregel ist {round(area_trapez, 2)}, die theoretische Abweichung ist {round(sum_dev_trapez, 2)}, die "
          f"praktische Abweichung ist {round(abs(area_real - area_trapez), 2)}")
    print(f"Die Fläche nach der Keplerregel ist {round(area_kepler, 2)}, die theoretische Abweichung ist {round(sum_dev_kepler, 2)}, die "
          f"praktische Abweichung ist {round(abs(area_real - area_kepler), 2)}\n")

def plot(t, n):
    h = x_kepler_vals[1]

    x_values = [x for x in np.linspace(0, t, 100)]
    real_func_values = [func(x) for x in x_values]
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

    ax[0].plot(x_values, real_func_values, label="f(x)")
    ax[0].plot(x_trapez_vals, trapez_vals, label="Approximation nach Trapezregel")
    if(t<=10):
        ax[0].scatter([i for i in np.linspace(0, t, n)], [func(i) for i in np.linspace(0, t, n)])
    ax[0].legend()

    ax[1].plot(x_values, real_func_values, label="f(x)")
    ax[1].plot(x_kepler_vals_curve, kepler_vals, label="Approximation nach Keplerregel")
    if(t<=10):
        ax[1].scatter([i for i in np.linspace(0, t, n)], [func(i) for i in np.linspace(0, t, n)])
    ax[1].legend()


    # plt.show()

interpolation(1, 10)
interpolation(1, 20)
interpolation(1, 40)
interpolation(1, 60)
interpolation(1, 90)
interpolation(1, 160)
