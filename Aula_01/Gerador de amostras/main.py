import numpy as np
import matplotlib.pyplot as plt

Dt = 5*(10**-5)
t = np.arange(-5*10**-3, 5*10**-3, Dt)

f = 400
xa = np.cos(2*np.pi*f*t)

plt.subplot(2,1,1)
plt.plot(t*1000,xa)
plt.xlabel('Tempo [ms]')
plt.ylabel('xa(t)')
title = 'Sinal de Freq = ' + str(f) + 'Hz'
plt.title(title)
plt.grid()

Fs = 5000
Ts = 1/Fs
n = np.arange(-20, 20, 1)
xd = np.cos(2*np.pi*n*f/Fs)
N = len(n)

plt.stem(n*Ts*1000,xd,'r')
plt.subplot(2,1,2)
plt.stem(n,xd)
plt.title('Sinal amostrado')
plt.xlabel('Amostras')
plt.ylabel('x[n]')
plt.grid()

plt.tight_layout()
plt.show()