import numpy as np
import matplotlib.pyplot as plt

#file = input("Nome do arquivo: ")
fc = float(input("Frequência de corte: "))
#with open(file, 'rb') as fid:
#    entrada = np.fromfile(fid, np.int16)
#fid.close()

entrada = np.ones(50)

pi = np.pi
print(pi)

# Função Sinc
h = np.zeros(len(entrada))
for i in range(1, len(entrada)):
     h[i] = (np.sin(2*pi*fc*i))/(i*pi)

plt.title("Função sinc para Fc = " + str(fc))
plt.plot(h, 'r')
plt.grid()
plt.show()
