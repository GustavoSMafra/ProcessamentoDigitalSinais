import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

M = int(input("M: "))

pi = np.pi

# Função Hamming
H = np.zeros(M)
for i in range(M):
     H[i] = 0.54 - (0.46 * (np.cos((2*pi*i)/M)))

# Função Blackman
B = np.zeros(M)
for i in range(M):
     B[i] = 0.42 - (0.5 * np.cos((2*pi*i)/M)) + (0.08 * np.cos((4*pi*i)/M))

plt.subplot(2, 2, 1)
plt.title("Hamming")
plt.plot(H, 'r')
plt.grid()

plt.subplot(2, 2, 2)
plt.title("Blackman")
plt.plot(B, 'r')
plt.grid()

plt.subplot(2,2,3)
plt.title("Black x Hamming")
plt.plot(B, 'r')
plt.plot(H, 'b')
plt.legend(['Blackman', 'Hamming'])
plt.grid()

plt.tight_layout()
plt.show()

fs = 8000

plt.subplot(2, 2, 1)
plt.title("Hamming")
[w1, L] = signal.freqz(H, 1, fs)
plt.plot(w1*fs/(2*np.pi), 20*np.log10(abs(L)))
plt.grid()

plt.subplot(2, 2, 2)
plt.title("Blackman")
[w2, J] = signal.freqz(B, 1, fs)
plt.plot(w2*fs/(2*np.pi), 20*np.log10(abs(J)))
plt.grid()

plt.subplot(2,2,3)
plt.title("Black x Hamming")
plt.plot(w1*fs/(2*np.pi), 20*np.log10(abs(L)),  'r')
plt.plot(w2*fs/(2*np.pi), 20*np.log10(abs(J)),  'b')
plt.legend(['Hamming', 'Blackman'])
plt.grid()

plt.tight_layout()
plt.show()

