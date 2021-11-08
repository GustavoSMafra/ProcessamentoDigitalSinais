import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

pi = np.pi
fc = .14
M = 100
H = np.zeros(100)

for i in range(100):
    if((i-M/2) == 0):
        H[i] = 2*pi*fc

    elif((i-M/2) != 0):
        H[i] = np.sin(2*pi*fc*(i-(M/2))) / (i-(M/2))

    H[i] = H[i] * (0.54 - 0.46 * np.cos(2 * pi * i/M))

sum = 0
for i in range(100):
    sum = sum + H[i]

for i in range(100):
    H[i] = H[i] / sum

'''
w, H = signal.freqz(H, 1, fc)
Freq = fc*w/(2*np.pi)
plt.plot(Freq, 20*np.log10(abs(H)))
plt.title('Magnitude da resposta em frequencia')
plt.show()
'''

print('Foram gerados: ' + str(len(H)) + ' pontos do windowed-sinc filter')
with open("Coef_PB.dat", "w") as f:
    for s in H:
        f.write(str(s) +",\n")



