import numpy as np
import matplotlib.pyplot as plt

opc = int(input('Sinal gerado \n[0]Impulso Unitário \n[1]Degrau Unitário \n[2]Sequência Sinusoidal \n[3]Sequência Exponencial: '))

n = np.arange(0, 30, 1)

if opc == 0:
    xn = []
    for i in range(len(n)):
        if n[i] == 0:
            xn.append(1)
        else:
            xn.append(0)

elif opc == 1:
    xn = []
    for i in range(len(n)):
        if n[i] >= 0:
            xn.append(1)
        else:
            xn.append(0)

elif opc == 2:
    f = int(input('Frequência: '))
    Fs = int(input('Frequência de amostragem: '))
    xn = np.cos(2*np.pi*n*f/Fs)

elif opc == 3:
    xn = []
    a = float(input('A: '))
    for i in range(len(n)):
        xn.append(a**(n[i]))

plt.xlabel('N')
plt.ylabel('xn(N)')
title = 'Sinal Gerado'
plt.title(title)
plt.stem(n, xn)
plt.grid()
plt.show()

textfile = open("SinalGerado.txt", "w")
for element in str(xn):
    textfile.write(element)
textfile.close()

