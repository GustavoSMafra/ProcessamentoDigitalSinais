import numpy as np

with open('Coef_BP.dat', 'r') as f:
    coefs = [line.strip().replace(',', '') for line in f]

coef_int = np.zeros(len(coefs))
for i in range(len(coefs)):
    coef_int[i] = int(float(coefs[i]) * 32768)

with open("Coef_BP_short.dat", "w") as f:
    for s in coef_int:
        f.write(str(s) +",\n")