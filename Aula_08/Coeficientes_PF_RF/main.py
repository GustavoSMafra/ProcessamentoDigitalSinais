import numpy as np
from scipy.signal import freqz
import matplotlib.pyplot as plt

pi = np.pi
fc1 = int(input("Frequência de corte 1: "))
fc2 = int(input("Frequência de corte 2: "))
fs = int(input("Frequência de amostragem: "))
B = int(input("Transição: "))

fc1 = fc1/fs
fc2 = fc2/fs
M = int(4/(B/fs))

PB1 = np.zeros(M)
PB2 = np.zeros(M)
PA = np.zeros(M)
BP = np.zeros(M)
BR = np.zeros(M)

# Low Pass
for i in range(M):
    if((i-M/2) == 0):
        PB1[i] = 2*pi*fc1

    elif((i-M/2) != 0):
        PB1[i] = np.sin(2*pi*fc1*(i-(M/2))) / (i-(M/2))

    PB1[i] = PB1[i] * (0.54 - 0.46 * np.cos(2 * pi * i/M))

sum = 0
for i in range(M):
    sum = sum + PB1[i]

for i in range(M):
    PB1[i] = PB1[i] / sum

# High Pass
for i in range(M):
    if((i-M/2) == 0):
        PB2[i] = 2*pi*fc2

    elif((i-M/2) != 0):
        PB2[i] = np.sin(2*pi*fc2*(i-(M/2))) / (i-(M/2))

    PB2[i] = PB2[i] * (0.54 - 0.46 * np.cos(2 * pi * i/M))

sum = 0
for i in range(M):
    sum = sum + PB2[i]

for i in range(M):
    PB2[i] = PB2[i] / sum

for i in range(M):
    PA[i] = -(PB2[i])

i = int(M / 2)
PA[i] = PA[i] + 1

# Band Reajeact
for i in range(M):
    BR[i] = PB1[i] + PA[i]

# Band pass
for i in range(M):
    BP[i] = -BR[i]
BP[int(M/2)] += 1

print('Foram gerados Passa Banda: ' + str(len(BP)) + ' pontos do windowed-sinc filter')
with open("Coef_BP.dat", "w") as f:
    for s in BP:
        f.write(str(s) +",\n")

print('Foram gerados Rejeita Banda: ' + str(len(BR)) + ' pontos do windowed-sinc filter')
with open("Coef_BR.dat", "w") as f:
    for s in BR:
        f.write(str(s) +",\n")

plt.subplot(2, 1, 1)
plt.title("Coeficientes PB")
plt.plot(PB1, 'r')
plt.subplot(2, 1, 2)
plt.title("Frequência PB")
w, G = freqz(PB1, 1, fs)
Freq = fs*w/(2*np.pi)
plt.plot(Freq, 20*np.log10(abs(G)))
plt.title('Magnitude da resposta em frequencia')
plt.tight_layout()
plt.show()

plt.subplot(2, 1, 1)
plt.title("Coeficientes PA")
plt.plot(PA, 'r')
plt.subplot(2, 1, 2)
plt.title("Frequência PA")
w, G = freqz(PA, 1, fs)
Freq = fs*w/(2*np.pi)
plt.plot(Freq, 20*np.log10(abs(G)))
plt.title('Magnitude da resposta em frequencia')
plt.tight_layout()
plt.show()

plt.subplot(2, 1, 1)
plt.title("Coeficientes PF")
plt.plot(BP, 'r')
plt.subplot(2, 1, 2)
plt.title("Frequência PF")
w, G = freqz(BP, 1, fs)
Freq = fs*w/(2*np.pi)
plt.plot(Freq, 20*np.log10(abs(G)))
plt.title('Magnitude da resposta em frequencia')
plt.tight_layout()
plt.show()

plt.subplot(2, 1, 1)
plt.title("Coeficientes RF")
plt.plot(BR, 'r')
plt.subplot(2, 1, 2)
plt.title("Frequência RF")
w, G = freqz(BR, 1, fs)
Freq = fs*w/(2*np.pi)
plt.plot(Freq, 20*np.log10(abs(G)))
plt.title('Magnitude da resposta em frequencia')
plt.tight_layout()
plt.show()