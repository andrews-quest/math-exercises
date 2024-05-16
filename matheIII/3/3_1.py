import matplotlib.pyplot as plt
import numpy as np

x_points = [0, 2, 4, 6, 8, 10]
y_points = [2, 5.8, 7, 5, 2, 1]

x_values = []
y_values_1 = []
y_values_2 = []
y_values_3 = []
y_values_4 = []
y_values_5 = []
y_values_6 = []
y_values = []

def find_polynome(x, k):
    result = 0
    numerator = 1
    denominator = 1
    for i in range(0, len(y_points)):
        numerator *= (x - x_points[i])
        if i == k:
            continue
        denominator *= (x_points[k] - x_points[i])
    result += numerator/denominator
    print(result)
    return result

for x in np.linspace(0, 10, 100):
    x_values.append(x)
    y_values_1.append(find_polynome(x,0) * y_points[0])
    y_values_2.append(find_polynome(x,1) * y_points[1])
    y_values_3.append(find_polynome(x,2) * y_points[2])
    y_values_4.append(find_polynome(x,3) * y_points[3])
    y_values_5.append(find_polynome(x,4) * y_points[4])
    y_values_6.append(find_polynome(x,5) * y_points[5])
    y_values.append(y_values_1[-1] +
                    y_values_2[-1] +
                    y_values_3[-1] +
                    y_values_4[-1] +
                    y_values_5[-1])

print(x_values)
print(y_values)

plt.legend()
plt.plot(x_values, y_values)
plt.plot(x_values, y_values_1)
plt.plot(x_values, y_values_2)
plt.plot(x_values, y_values_3)
plt.plot(x_values, y_values_4)
plt.plot(x_values, y_values_5)
plt.show()