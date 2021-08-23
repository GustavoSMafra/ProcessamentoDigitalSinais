import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg

sg.change_look_and_feel('DarkGrey2')

layout = [
    [sg.Text('Frequência em Hz'),sg.Input(size=(10,0), key= 'f')],
    [sg.Text('Frequência de amostragem em Hz'), sg.Input(size=(10,0), key= 'Fs')],
    [sg.Text('Tempo de amostragem em segundos'), sg.Input(size=(10,0), key= 'T')],
    [sg.Text('N inicial'), sg.Input(size=(10,0), key= 'N')],
    [sg.Text('Valor de A'), sg.Input(size=(10, 0), key='A')],
    [sg.Checkbox('Cos', key= 'Cos'), sg.Checkbox('Sen', key= 'Sen')],
    [sg.Checkbox('Impulso Unitário', key= 'IU'), sg.Checkbox('Degrau Unitário', key= 'DU'), sg.Checkbox('Sequência Sinusoidal', key= 'SS'), sg.Checkbox('Sequência Exponencial', key= 'SE')],
    [sg.Text('Nome do arquivo gerado'),sg.Input(size=(20,0), key= 'Nome')],
    [sg.Button('Gerar Sinal')]
]
janela = sg.Window('Gerador de Sinais', size=(650, 400),element_justification='l').layout(layout)
event, value = janela.read()
while True:
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Gerar Sinal':
        f = float(value['f'])
        Fs = float(value['Fs'])
        T = float(value['T'])
        Ninicial = int(value['N'])
        a = float(value['A'])

        Nfinal = int(T*Fs)
        n = np.arange(Ninicial, Nfinal-1, 1)
        xn = []

        if value['IU'] == True:
            for i in range(len(n)):
                if n[i] == 0:
                    xn.append(1)
                else:
                    xn.append(0)

        elif value['DU'] == True:
            for i in range(len(n)):
                if n[i] >= 0:
                    xn.append(1)
                else:
                    xn.append(0)

        elif value['SS'] == True:
            if value['Sen'] == True:
                xn = np.sin(2*np.pi*n*f/Fs)
            elif value['Cos'] == True:
                xn = np.cos(2*np.pi*n*f/Fs)

        elif value['SE'] == True:
            for i in range(len(n)):
                xn.append(a**(n[i]))

        plt.xlabel('N')
        plt.ylabel('xn(N)')
        title = 'Sinal Gerado'
        plt.title(title)
        plt.stem(n, xn)
        plt.grid()
        plt.show()

        nome = str(value['Nome']) + '.pcm'
        with open(nome, 'w') as fid:
            np.array(xn, dtype=np.int16).tofile(fid)
        fid.close()
        event, value = janela.read()