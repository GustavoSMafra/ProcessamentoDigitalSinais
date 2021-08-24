import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg

sg.change_look_and_feel('DarkGrey2')

layout = [
    [sg.Text('FS'), sg.Input(size=(10, 0), key='FS')],
    [sg.Text('D  '), sg.Input(size=(10, 0), key='D')],
    [sg.Text('A0'), sg.Input(size=(10, 0), key='A0')],
    [sg.Text('A1'), sg.Input(size=(10, 0), key='A1')],
    [sg.Text('       Nome sinal entrada'), sg.Input(size=(20, 0), key='Entrada')],
    [sg.Text('Nome do arquivo gerado'), sg.Input(size=(20, 0), key='Nome')],
    [sg.Checkbox('Salvar arquivo', key='Salvar')],
    [sg.Button('Gerar modificação')]
]
janela = sg.Window('Eco', size=(400, 400), element_justification='l').layout(layout)
event, value = janela.read()

while True:
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Gerar modificação':

        file_entrada = str(value['Entrada'])
        with open(file_entrada, 'rb') as fid:
            entrada = np.fromfile(fid, np.int16)
        fid.close()

        Fs = float(value["FS"])
        D = float(value["D"])
        n = int(Fs * D)

        a0 = float(value["A0"])
        a1 = float(value["A1"])

        sinal_saida = np.zeros(len(entrada))

        for i in range(len(entrada)):
            sinal_saida[i] = (a0 * entrada[i] + a1 * sinal_saida[i - n])

        n = np.arange(0, len(entrada), 1)

        plt.subplot(2, 1, 1)
        plt.stem(n, entrada)
        plt.title("Sinal de entrada")
        plt.grid()
        plt.subplot(2, 1, 2)
        plt.stem(n, sinal_saida, 'r')
        plt.title("Sinal com Eco")
        plt.grid()
        plt.tight_layout()
        plt.show()

        if value['Salvar'] == True:
            nome = value['Nome']
            with open(nome, 'w') as fid:
                np.array(sinal_saida, dtype=np.int16).tofile(fid)
            fid.close()
        event, value = janela.read()
