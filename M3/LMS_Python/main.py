import numpy as np
import matplotlib.pyplot as plt

# Carregar Coeficientes
with open('Coefs_MM_8.dat', 'r') as f:
    coefs= [line.strip().replace(',', '') for line in f]

coef = np.zeros(len(coefs))
for i in range(len(coefs)):
    coef[i] = np.float64(coefs[i].split(','))

# Carregar Entrada
with open('ruido_branco.pcm', 'rb') as fid:
    x = np.fromfile(fid, np.int16)
fid.close()

print(len(x))

u = 0.000000000005
K = 20
N = len(x)

d = np.zeros(len(x))
e = np.zeros(len(x))
y = np.zeros(len(x))
w = np.zeros(K)

amostrasD = np.zeros(len(coef))
amostrasY = np.zeros(len(w))

########################################################
# Sinal Esperado
for i in range(len(x)):
    for j in range(len(coef)):
        if (i - j) >= 0:
            amostrasD[j] = x[i - j] * float(coef[j])
    d[i] = amostrasD.sum()

########################################################


for i in range(len(x)):
    for j in range(len(w)):
        if (i - j) >= 0:
            amostrasY[j] = x[i-j] * float(w[j])
    y[i] = amostrasY.sum()

    e[i] = d[i] - y[i]

    for k in range(len(w)):
        if (i - k) >= 0:
            w[k] = w[k] + (u * e[i] * x[i-k])

plt.subplot(2,1,1)
plt.plot(d, 'b')
plt.title("Entrada")
plt.grid()
plt.subplot(2,1,2)
plt.plot(y, 'r')
plt.title("Saída")
plt.grid()
plt.tight_layout()
plt.show()

plt.plot(e, 'r')
plt.title("Erro")
plt.grid()
plt.show()

print(w)

with open("saida_py.pcm", 'w') as fid:
    np.array(y, dtype=np.int16).tofile(fid)
fid.close()