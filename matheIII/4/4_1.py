import numpy as np
import matplotlib.pyplot as plt




def func(x):
    return (x**2 + 3)*(np.e**(2*x))

def w(f):
    pass

trapez_vals = []
x_trapez_vals = []

def trapez(w, t, n):
    global x_trapez_vals
    x_trapez_vals = [x_n for x_n in np.linspace(0, t, n)]
    for x_n in x_trapez_vals:
       trapez_vals.append(func(x_n))

def interpolation(w, t, n):
    trapez(w, t, n)
    plot()

x_values = [x for x in np.linspace(-10, 20, 100)]
real_func_values = [func(x) for x in x_values]

def plot():
    fig = plt.figure()
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.plot(x_values, real_func_values)
    ax.plot(x_trapez_vals, trapez_vals)

    plt.show()

    print(x_values)
    print(real_func_values)

interpolation(0, 20, 5)

# 3.0, 4.574800863631075, 7.163395637649524, 11.482668850715338, 18.762502242204484, 31.104923710965092, 52.087143263512715, 87.7692222784067, 148.37029791219274, 251.04518883457058, 424.4656666762457, 716.3516125304421, 1205.8090849099094, 2023.4787159308455, 3384.340101884782, 5640.972243083461, 9369.798800605415, 15510.401732403157, 25590.035879354342, 42084.66242092909, 68998.32022908628, 112791.07405403799, 183862.53704892844, 298919.48701132083, 484748.2430684048, 784215.9233588767, 1265803.3930127951, 2038727.0023473632, 3276893.541548143, 5256799.936084059, 8417422.450896274, 13454744.121133177, 21470789.01775878, 34208344.58642138, 54420264.33119289, 86449949.83629435, 137142922.31082764, 217277049.01376256, 343804598.4971217, 543364041.0826988, 857776331.9364561, 1352640527.894427, 2130766569.146152, 3353152474.477385, 5271720855.141566, 8280373106.448077, 12994560300.928795, 20375222850.854046, 31921724415.99029, 49972015127.20834]
