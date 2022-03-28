from PySimpleGUI import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome', sg.Input())],
            [sg.Text('Idade'), sg.Input()],
            [sg.Button('Enviar Dados')]
        ]
        #Janela
        janela = sg.Window('Dados do usuario').layout(layout)
        #Extrair os dados da tela
        self.button, self.value = janela.Read()
        
    def Iniciar(self):
        print(self.value)
        
tela = TelaPython()
tela.Iniciar()
        