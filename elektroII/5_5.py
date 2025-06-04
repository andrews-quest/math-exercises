import matplotlib.pyplot as plt
import numpy
import labellines

freq = [0.5, 1, 1.2, 1.5, 2, 2.5, 3, 3.5, 4.0]
I = [1.8, 5.2, 8.3, 20.1, 10, 5.2, 3.7, 2.9, 2.4]
U_C = [5.5, 8.1, 11, 21.1, 19, 3.3, 1.8, 1.3, 0.9]
U_L = [0.5, 3.1, 6, 18.5, 12.5, 8.1, 6.8, 6.1, 6]

plt.plot(freq, I)
plt.plot(freq, U_C)
plt.plot(freq, U_L)



plt.xlabel("Frequenz (KHz)")
plt.ylabel("")
plt.yticks(rotation=45)
plt.show()