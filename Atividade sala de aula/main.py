import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg

sg.change_look_and_feel('DarkGrey2')

layout = [
    [sg.Checkbox('PA', key='PA')],
    [sg.Checkbox('PB', key='PB')],
    [sg.Text('       Nome sinal entrada'), sg.Input(size=(20, 0), key='Entrada')],
    [sg.Text('Nome do arquivo gerado'), sg.Input(size=(20, 0), key='Nome')],
    [sg.Checkbox('Salvar arquivo', key='Salvar')],
    [sg.Button('Gerar modificação')]
]
janela = sg.Window('Média Móvel', size=(400, 400), element_justification='l').layout(layout)
event, value = janela.read()

while True:
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Gerar modificação':

        file_entrada = str(value['Entrada'])
        with open(file_entrada, 'rb') as fid:
            entrada = np.fromfile(fid, np.int16)
        fid.close()

        #Armazenar os valores de coenficiente
        if(value['PA'] ):
            with open('Coefs_PA_1k.dat', 'r') as f:
                coenfs= [line.strip() for line in f]

        if (value['PB']):
            with open('Coefs_PB_1k.dat', 'r') as f:
                coenfs= [line.strip() for line in f]

        k = len(coenfs)
        tam = len(entrada)
        sinal_saida = []
        amostras = np.zeros(k, dtype=float)

        for i in range(tam):
            for j in range(k):
                if (i - j) >= 0:
                    amostras[j] = entrada[i - j] * np.float64(coenfs[j])
            sinal_saida.append(amostras.sum())

        plt.subplot(2, 1, 1)
        plt.plot(entrada)
        plt.title("Sinal de entrada")
        plt.grid()
        plt.subplot(2, 1, 2)
        plt.plot(sinal_saida, 'r')
        plt.title("Sinal Média móvel")
        plt.grid()
        plt.tight_layout()
        plt.show()

        if value['Salvar'] == True:
            nome = value['Nome']
            with open(nome, 'w') as fid:
                np.array(sinal_saida, dtype=np.int16).tofile(fid)
            fid.close()
        event, value = janela.read()
