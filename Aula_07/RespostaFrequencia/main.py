import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import signal

passo = np.pi / 1000
w = np.arange(0, np.pi, passo)
L = 8
Fs = 8000

opc = input("Qual exercício: ")

if opc == "Exemplo":
    num = np.sin(w * L / 2)
    den = np.sin(w / 2)

elif opc == "4-A":
    #Questão 4-A
    num = 3*(np.exp(1j*w) - 1.2)
    den = (np.exp(1j*w)-0.5)*(np.exp(1j*w)-0.9)

elif opc == "4-B":
    #Questão 4-B
    num = np.exp(1j*w)
    den = (np.exp(1j*w) - 0.9)*(np.exp(1j*w) - 1.2)

elif opc == "4-C":
    #Questão 4-C

    num = (np.exp(1j*w) + 0.9)
    den = ((np.exp(1j*w)**2) + np.exp(1j*w)  + 0.41)

temp = num/den

X = (1 / L) * (abs(temp))
plt.subplot(3, 1, 1)
plt.plot(w, X)
plt.xlabel('Frquência')
plt.title('Frequêncua Rad')
plt.grid()


F_Hz = (w / np.pi) * (Fs / 2)
plt.subplot(3, 1, 2)
plt.plot(F_Hz, X)
plt.xlabel('Frequência')
plt.title('Frequência em Hz')
plt.grid()

X_Db = 20 * np.log10(X)
plt.subplot(3, 1, 3)
plt.plot(F_Hz, X_Db)
plt.ylabel('Atenuação DB')
plt.xlabel('Frequência')
plt.title('Frequência em Hz')
plt.grid()

plt.axis([0, 4000, - 70, 0])
num = np.zeros(L)
num[0:] = 1 / L
den = [1]
[w, H] = signal.freqz(num, den, Fs)
Freq = Fs * w / (2*np.pi)
plt.plot(Freq * Fs / (2 * np.pi), 20 * np.log10(abs(H)))
plt.title('Magnitude da resposta em frequencia')

plt.tight_layout()
plt.show()