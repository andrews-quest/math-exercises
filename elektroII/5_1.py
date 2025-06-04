import matplotlib.pyplot as plt
import numpy

freq = [0.5, 1, 1.5, 2, 4, 6]
R = [1000, 1000, 1000, 1000, 1000, 1000]
L = [125, 281, 388, 526, 1000, 1500]
C = [333, 158, 107, 79, 48, 43]

plt.plot(freq, R)
plt.plot(freq, L)
plt.plot(freq, C)

plt.xlabel("Frequenz (KHz)")
plt.ylabel("Z (Ω)")
plt.yticks(rotation=45)
plt.show()