import numpy as np
import matplotlib.pyplot as plt

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
