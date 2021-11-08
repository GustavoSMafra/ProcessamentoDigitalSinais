import numpy as np
import matplotlib.pyplot as plt

#Ganho
K = 1

M = int(input("M: "))
fc = float(input("FC: "))

pi = np.pi

# Função Windowed-sine
H = np.zeros(M)
for i in range(M):
     if(i == M/2):
          H[i] = 2*pi*fc*K
     else:
          H[i] = K * ((np.sin(2*pi*fc*(i - (M/2))))/(i - (M/2))) * (0.42 - (0.5 * np.cos((2*pi*i)/M)) + (0.08 * np.cos((4*pi*i)/M)))

plt.title("Windowed-sinc")
plt.plot(H, 'r')
plt.grid()
plt.show()
