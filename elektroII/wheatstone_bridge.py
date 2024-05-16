import matplotlib.pyplot as plt
import numpy as np

U_0 = 100
R_4 = 4
R_3 = 3
R_N = 5
resistances = []
fractions = []

for R_X in np.linspace(0, 10, 100):
    U_C = U_0*(R_N/(R_N + R_X))
    U_D = U_0*(R_4/(R_4 + R_3))

    U = U_C - U_D
    fractions.append(U / U_0)
    resistances.append(R_X)

plt.plot(fractions, resistances)
plt.xlabel("Ucd/Uab")
plt.ylabel("Rx", rotation=0)
plt.show()
