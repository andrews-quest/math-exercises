import numpy as np
import pandas as pd

# Gegebene Werte
R = 220  # Ohm
L = 100e-3  # Henry
C = 100e-9  # Farad
U = 5  # Volt
frequencies_kHz = np.array([0.5, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])  # kHz
frequencies_Hz = frequencies_kHz * 1e3

# Berechnungen
omega = 2 * np.pi * frequencies_Hz
X_L = omega * L
X_C = 1 / (omega * C)
Z = np.sqrt(R**2 + (X_L - X_C)**2)
I = U / Z
U_C = I * X_C
U_L = I * X_L

# Tabelle erstellen
df = pd.DataFrame({
    'Frequenz (kHz)': frequencies_kHz,
    'U_C (V)': U_C,
    'U_L (V)': U_L
})

df.round(3)

print(X_L)
print(X_C)
print(Z)
