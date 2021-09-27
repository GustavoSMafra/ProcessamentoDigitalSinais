import numpy as np
import matplotlib.pyplot as plt

a = .5
w = np.arange(-3*np.pi, 3*np.pi, np.pi/100)

Num =  np.exp(1j*w) + 1 + np.exp(-1j*w) # Numerador
Den = 1 # Denominador
X = Num/Den

Mod_X = abs(X)
Fase_X = np.angle(X)

plt.subplot(2,1,1)
plt.plot(w, Mod_X)
plt.title('Módulo de X')
plt.xlabel('W')
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(w, Fase_X)
plt.title('Fase de X')
plt.xlabel('W')
plt.grid(True)

print(Mod_X)

plt.tight_layout()
plt.show()