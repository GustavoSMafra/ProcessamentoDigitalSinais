import numpy as np
import matplotlib.pyplot as plt

with open('voz.pcm', 'rb') as fid:
    s = np.fromfile(fid, np.int16)
fid.close()

itera = s.size
sav_y = np.zeros(itera)
ganho = 0.5

for j in range (itera):
    sav_y[j] = s[j] * ganho

plt.subplot(2,1,1)
plt.plot(s)
plt.title("Sinal de entrada")
plt.grid()

plt.subplot(2,1,2)
plt.plot(sav_y, 'r')
plt.title("Saída")
plt.xlabel('Número de amostras')
plt.ylabel('Amplitude da saída')
plt.grid()

plt.tight_layout()
plt.show()

with open('sinal_saida.pcm', 'wb') as fid:
    np.array(sav_y, dtype=np.int16).tofile(fid)
fid.close()