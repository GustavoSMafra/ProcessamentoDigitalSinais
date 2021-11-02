import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from scipy import signal


sg.change_look_and_feel('DarkGrey2')

layout = [
    [sg.Text("Numerador:    "), sg.Input(size=(20, 0), key = 'Num')],
    [sg.Text("Denominador: "), sg.Input(size=(20, 0), key = 'Den')],
    [sg.Listbox(['Exemplo', '4-A', '4-B', '4-C', 'Passa baixa', 'Passa alta' , 'Valores alocados'], size=(20,7), key = "List")],
    [sg.Button("Calcular")]
]

janela = sg.Window('Respota em frequência', size=(400, 300), element_justification='l').layout(layout)
event, values = janela.read()

while True:
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Calcular":
        opc = (values["List"])
        Fs = 8000

        if opc[0] == "Exemplo":
            L = 8
            num = np.zeros(L)
            num[0:] = 1 / L
            #num = [0.1, 0.2, 0.4, 0.2, 0.1]
            #den = 1

        elif opc[0] == "4-A":
            #Questão 4-A
            num = [0, 3, -3.6]
            den = [1, -1.4, 0.45]

        elif opc[0] == "4-B":
            #Questão 4-B
            num = [0, 1, 0]
            den = [1, -2.1, 1.08]

        elif opc[0] == "4-C":
            #Questão 4-C
            num = [0, 1, 0.9]
            den = [1, 1, 0.41]

        elif opc[0] == "Passa baixa":
            #Questão 4-C
            num = [0, 6280, 6280]
            den = [0, 22280, -9720]

        elif opc[0] == "Passa alta":
            #Questão 4-C
            num = [0, 16000, -16000]
            den = [0, 22280, -9720]

        elif opc[0] == "Valores alocados":
            #Qualquer expressão colocada
            num = list(map(float, values["Num"].split(',')))
            den = list(map(float, values["Den"].split(',')))
            print(num)
            print(den)

        w, H = signal.freqz(num, den, Fs)
        Freq = Fs*w/(2*np.pi)
        plt.plot(Freq, 20*np.log10(abs(H)))
        plt.title('Magnitude da resposta em frequencia')

        plt.show()
        event, values = janela.read()