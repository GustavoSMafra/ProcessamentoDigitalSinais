import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg

sg.change_look_and_feel('DarkGrey2')

layout = [
    [sg.Text('FS'), sg.Input(size=(10, 0), key='FS')],
    [sg.Text('T1'), sg.Input(size=(10, 0), key='T1')],
    [sg.Text('T2'), sg.Input(size=(10, 0), key='T2')],
    [sg.Text('A0'), sg.Input(size=(10, 0), key='A0')],
    [sg.Text('A1'), sg.Input(size=(10, 0), key='A1')],
    [sg.Text('A1'), sg.Input(size=(10, 0), key='A2')],
    [sg.Text('       Nome sinal entrada'), sg.Input(size=(20, 0), key='Entrada')],
    [sg.Text('Nome do arquivo gerado'), sg.Input(size=(20, 0), key='Nome')],
    [sg.Checkbox('Salvar arquivo', key='Salvar')],
    [sg.Button('Gerar modificação')],
    [sg.Button('Voltar')]
]
janela = sg.Window('Delay', size=(400, 400), element_justification='l').layout(layout)
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
        t1 = float(value["T1"])
        t2 = float(value["T2"])

        n1 = int(t1 * Fs)
        n2 = int(t2 * Fs)

        a0 = float(value["A0"])
        a1 = float(value["A1"])
        a2 = float(value["A2"])

        vetor_delay = np.zeros(n2)
        sinal_saida = np.zeros(len(entrada))

        for i in range(len(entrada)):
            vetor_delay[0] = entrada[i]
            y = a0 * vetor_delay[0] + a1 * vetor_delay[n1 - 1] + a2 * vetor_delay[n2 - 1]
            for j in range(n2):
                vetor_delay[n2 - j - 1] = vetor_delay[n2 - j - 2]

            sinal_saida[i] = y

        n = np.arange(0, len(entrada), 1)

        plt.subplot(2, 1, 1)
        plt.stem(n, entrada)
        plt.title("Sinal de entrada")
        plt.grid()
        plt.subplot(2, 1, 2)
        plt.stem(n, sinal_saida, 'r')
        plt.title("Sinal com Delay")
        plt.grid()
        plt.tight_layout()
        plt.show()

        if value['Salvar'] == True:
            nome = value['Nome']
            with open(nome, 'w') as fid:
                np.array(sinal_saida, dtype=np.int16).tofile(fid)
            fid.close()
        event, value = janela.read()

    elif event == 'Voltar':
        janela.close()
        break