import matplotlib.pyplot as plt
import numpy as np

U_0 = 10
U_3 = 0
R_3 = [0, 1, 10]
R = 1
k = 0
fractions1 = []
fractions2 = []
fractions3 = []
ks = []

for k in np.linspace(0.01, 1, 100):
    U_3 = (U_0*(k*R + R_3[0]))/((1-k)*R+1)
    fractions1.append(U_3/U_0)

    U_3 = R_3[1]/(k*R)
    fractions2.append(U_3/U_0)

    U_3 = R_3[2]/(k*R)
    fractions3.append(U_3/U_0)

    ks.append(k)

plt.plot(ks, fractions1)
plt.plot(ks, fractions2)
plt.plot(ks, fractions3)
plt.legend(["R3 = 0", "R3 = 1", "R3 = 10"])
plt.xlabel("k")
plt.ylabel("U3/U", rotation=0)
plt.show()
