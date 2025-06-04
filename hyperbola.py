import matplotlib.pyplot as plt

x_vals = []
f_1_vals = []
f_2_vals = []
hyper_vals = []

for x in range(-50, 50):

    x_vals.append(x)
    f_1_vals.append(2*x+1)
    f_2_vals.append(2*x+2)
    hyper_vals.append(f_1_vals[-1] / (f_2_vals[-1]+0.01))


plt.plot(x_vals, f_1_vals, color="#3300FF", label="f1")
plt.plot(x_vals, f_2_vals, color="#00DD12", label="f2")
plt.plot(x_vals, hyper_vals, color="#BB1100", label="hyperbola")
plt.show()