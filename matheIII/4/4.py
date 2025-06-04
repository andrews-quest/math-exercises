import numpy as np

area_real = 0
area_trapez = 0
area_kepler = 0

sum_dev_trapez = 0
sum_dev_kepler = 0

t = 1
n_vals = [11, 21, 41, 63, 81, 161, 321]

def deviation_kepler(h, x):
    return (h**5) / 90 * abs(80 * np.e**(2*x))

def deviation_trapez(h, x):
    return (h**3) / 12 * abs(20 * np.e**(2*x))

def func(x):
    return np.float64(((x**2) + 3)*(np.e ** (2*x)))

def area_real_func(x):
    return (1/4) * (2*(x**2)-2*x+7) * (np.e**(2*x)) - (7/4)

def trapez(t, n):
    x_trapez_vals = [x_n for x_n in np.linspace(0, t, n)]
    y_prev = func(x_trapez_vals[0])
    h = x_trapez_vals[1]
    area_trapez = 0
    sum_dev_trapez = 0
    for x_n in x_trapez_vals[1:]:
        area_trapez += (h/2)*(func(x_n) + y_prev)
        y_prev = func(x_n)
        sum_dev_trapez += deviation_trapez(h, x_n)
    return area_trapez, sum_dev_trapez

def kepler(t, n):
    x_kepler_vals= [x_n for x_n in np.linspace(0, t, n)]
    h = x_kepler_vals[2] - x_kepler_vals[0]
    area_kepler = 0
    sum_dev_kepler = 0
    for i in range(0, n-2, 2):
        area_kepler += np.float64((h/6)*(func(x_kepler_vals[i]) + (func(x_kepler_vals[i+1]) * 4) + func(x_kepler_vals[i+2])))
        sum_dev_kepler += deviation_kepler(h, x_kepler_vals[i+2])
    return area_kepler, sum_dev_kepler

def print_result():
    print(f"Die Fläche nach der Trapezregel ist {round(area_trapez, 3)}, die theoretische Abweichung ist {round(sum_dev_trapez, 20)}, die "
           f"praktische Abweichung ist {round(abs(area_real - area_trapez), 20)}")
    print(f"Die Fläche nach der Keplerregel ist {round(area_kepler, 8)}, die theoretische Abweichung ist {round(sum_dev_kepler, 20)}, die "
           f"praktische Abweichung ist {round(abs(area_real - area_kepler), 20)}\n")


area_real = area_real_func(t)
print(f"Die Fläche unter dem Graph beträgt {round(area_real, 8)}\n")

for n in n_vals:
    area_trapez, sum_dev_trapez = trapez(t, n)
    area_kepler, sum_dev_kepler = kepler(t, n)
    print_result()

    area_kepler = 0
    area_trapez = 0
    sum_dev_kepler = 0
    sum_dev_trapez = 0