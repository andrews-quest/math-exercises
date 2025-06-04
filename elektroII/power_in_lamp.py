import numpy as np
import matplotlib.pyplot as plt

U = (1, 2, 4, 6, 8, 10, 12)
P_mess = (0.1, 0.4, 1.5, 2.8, 4.6, 6.4, 8.7)

I = (18, 264, 395, 495, 586, 659, 733)
R_ber = (5.6, 7.58, 10.13, 12.12, 13.56, 15.17, 16.36)
P_ber = (0.18, 0.53, 1.58, 2.97, 4.69, 6.6, 8.8)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(6, 6))
ax[0].plot(U, P_mess)
ax[0].set_xlabel("Spannung (V)")
ax[0].set_ylabel("Abgemessene Leisung (W)")

ax[1].plot(I, R_ber)
ax[1].set_xlabel("Strom (mA)")
ax[1].set_ylabel("Berechteter Widerstand (Ohm)")

ax[2].plot(I, P_ber)
ax[2].set_xlabel("Strom (mA)")
ax[2].set_ylabel("Berechnete Leistung (W)")
plt.show()
