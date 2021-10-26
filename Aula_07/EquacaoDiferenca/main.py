import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg

sg.change_look_and_feel('DarkGrey2')

layout = [
    [sg.Checkbox('PB', key='PB')],
    [sg.Checkbox('PA', key='PA')],
    [sg.Text('\t\tValor de Fc'), sg.Input(size=(10, 0), key='Fc')],
    [sg.Text('\t\tValor de Fs'), sg.Input(size=(10, 0), key='Fs')],
    [sg.Text('       Nome sinal entrada'), sg.Input(size=(20, 0), key='Entrada')],
    [sg.Text('Nome do arquivo gerado'), sg.Input(size=(20, 0), key='Nome')],
    [sg.Button('Calcular')]
]
janela = sg.Window('Equação Diferença', size=(400, 400), element_justification='l').layout(layout)
event, value = janela.read()

while True:
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Calcular':

        file_entrada = str(value['Entrada'])
        with open(file_entrada, 'rb') as fid:
            x = np.fromfile(fid, np.int16)
        fid.close()

        if (value['PB'] == 1):
            opc = 1
        elif (value['PA'] == 1):
            opc = 2
        else:
            opc = 3

        ynm1 = 0
        xnm1 = 0

        Fc = float(value['Fc'])
        Fs = float(value['Fs'])
        Wc = 2 * np.pi * Fc
        Fli = 2 * Fs

        tamaloop = len(x)
        vet_saida = np.zeros(tamaloop)

        if(opc == 1):
            a = Wc / (Fli + Wc)
            b = (Wc - Fli) / (Fli + Wc)

            for j in range(1,tamaloop):
                input = x[j]
                y = a * input + a * xnm1 - b * ynm1
                ynm1 = y
                xnm1 = input
                vet_saida[j]= y

        elif (opc == 2):
            a = Fli/(Fli + Wc)
            b = (-Fli + Wc) / (Fli + Wc)

            for j in range(1, tamaloop):
                input = x[j]
                y = a * input - a * xnm1 - b * ynm1
                ynm1 = y
                xnm1 = input
                vet_saida[j] = y

        else:
            print("Escolha um tipo de filtro")

        with open(value['Nome'], 'w') as fid:
            np.array(vet_saida, dtype=np.int16).tofile(fid)
        fid.close()

        plt.plot(x, 'b')
        plt.plot(vet_saida, 'r', linewidth=2)
        plt.grid
        plt.show()
        event, value = janela.read()





