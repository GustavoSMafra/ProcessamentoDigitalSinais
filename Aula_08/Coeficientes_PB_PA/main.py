import numpy as np
from scipy.signal import freqz
import matplotlib.pyplot as plt

pi = np.pi
fc = int(input("Frequência de corte: "))
fs = int(input("Frequência de amostragem: "))
B = int(input("Transição: "))

fc = fc/fs
M = int(4/(B/fs))
H = np.zeros(M)

# Low Pass
for i in range(M):
    if((i-M/2) == 0):
        H[i] = 2*pi*fc

    elif((i-M/2) != 0):
        H[i] = np.sin(2*pi*fc*(i-(M/2))) / (i-(M/2))

    H[i] = H[i] * (0.54 - 0.46 * np.cos(2 * pi * i/M))

sum = 0
for i in range(M):
    sum = sum + H[i]

for i in range(M):
    H[i] = H[i] / sum

# High Pass
H2 = np.zeros(M)
for i in range(M):
    H2[i] = -(H[i])

i = int(M/2)
H2[i] = H2[i] + 1

# Salvamento dos coeficientes em arquivo
print('Foram gerados PB: ' + str(len(H)) + ' pontos do windowed-sinc filter')
with open("Coef_PB.dat", "w") as f:
    for s in H:
        f.write(str(s) +",\n")

print('Foram gerados PA: ' + str(len(H)) + ' pontos do windowed-sinc filter')
with open("Coef_PA.dat", "w") as f:
    for s in H2:
        f.write(str(s) +",\n")

# Plot dos valores obtidos
plt.subplot(2, 1, 1)
plt.title("Coeficientes PB")
plt.plot(H, 'r')
plt.subplot(2, 1, 2)
plt.title("Frequência PB")
w, G = freqz(H, 1, fs)
Freq = fs*w/(2*np.pi)
plt.plot(Freq, 20*np.log10(abs(G)))
plt.title('Magnitude da resposta em frequencia')
plt.tight_layout()
plt.show()

plt.subplot(2, 1, 1)
plt.title("Coeficientes PA")
plt.plot(H2, 'r')
plt.subplot(2, 1, 2)
plt.title("Frequência PA")
w, G = freqz(H2, 1, fs)
Freq = fs*w/(2*np.pi)
plt.plot(Freq, 20*np.log10(abs(G)))
plt.title('Magnitude da resposta em frequencia')
plt.tight_layout()
plt.show()