import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fc = 0.25
M = 150
h = np.zeros(M)
x = np.arange(-M/2, M/2, 1)

for i in range(M):
    if i == M/2:
        h[i] = 1
    if i < M/2:
        h[i] = (np.sin(2 * np.pi * fc * (-i+M/2))) / ((-i+M/2) * np.pi)
    elif i > M/2:
        h[i] = (np.sin(2 * np.pi * fc * (i-M/2))) / ((i-M/2) * np.pi)


plt.plot(x, h, 'r')
plt.title('Função Sinc')
plt.grid()
plt.show()

fs = 8000
plt.title("Resposta em frequência Sinc")
[w, J] = signal.freqz(h, 1, fs)
plt.plot(w*fs/(2*np.pi), 20*np.log10(abs(J)))
plt.grid()
plt.show()
