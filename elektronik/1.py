import matplotlib.pyplot as plt
import numpy as np

# Eingangsspannung und Ausgangsspannung

U_E1 = [u for u in np.linspace(0, 5, 24)]
U_A1 = [3.54, 3.5, 3.42, 1.43, 1.16, 0.87, 0.63, 0.63, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]

U_E12 = [u for u in np.linspace(5, 0, 9)]
U_A12 = [0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 1.3, 3.48]

U_E2 = [u for u in np.linspace(5, 0, 25)]
I_E2 = [-1.29, -1.22, -1.18, -1.11, -1.04, -0.90, -0.80, -0.75, -0.08, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0.1,]

I_A3 = [i for i in np.linspace(0.25, 0.6, 19)]
U_A3 = [3.67, 3.66, 3.65, 3.64, 3.63, 3.63, 3.63, 3.62, 3.61, 3.61, 3.60, 3.59, 3.59, 3.59, 3.59, 3.59, 3.59, 3.59, 3.58]

U_A4 = [u for u in np.linspace(146, 60, 18)]
I_A4 = [i for i in np.linspace(-14.6, -6.0, 18)]


figure, axis = plt.subplots(2, 3)

axis[0, 0].plot(U_E1, U_A1)
axis[0, 0].set_xlabel("$U_E, V$")
axis[0, 0].set_ylabel("$U_A, V$")


axis[0, 1].plot(U_E12, U_A12)
axis[0, 1].set_xlabel("$U_E, V$")
axis[0, 1].set_ylabel("$U_A, mI$")
axis[0, 1].set_xlim(max(U_E12)+0.5, min(U_E12)-0.5)

axis[0, 2].plot(U_E2, I_E2)
axis[0, 2].set_xlabel("$U_A, V$")
axis[0, 2].set_ylabel("$I_A, mI$")
axis[0, 2].set_xlim(max(U_E2)+0.5, min(U_E2)-0.5)

axis[1, 0].plot(I_A3, U_A3)
axis[1, 0].set_xlabel("$U_A, V$")
axis[1, 0].set_ylabel("$I_A, mI$")
axis[1, 0].set_xlim(max(I_A3)+0.05, min(I_A3)-0.05)

axis[1, 1].plot(U_A4, I_A4)
axis[1, 1].set_xlabel("$U_A, mV$")
axis[1, 1].set_ylabel("$I_A, mI$")
axis[1, 1].set_xlim(max(U_A4)+5, min(U_A4)-5)
plt.show()

