import PySimpleGUI  as sg

class TelaPython:
    def __init__(self):
        # layout
        layout = [
        [sg.Text('Nome:'), sg.Input(size=20, key = 'nome')],
        [sg.Text('Idade:'), sg.Input(size=20, key = 'idade') ],
        [sg.Text('Quais provedores de e-mail sao aceitos?')],
        [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key = 'outlook'), sg.Checkbox('Yahoo', key = 'yahoo')],
        [sg.Button('Enviar Dados')],
        ]
        # Janela
        janela = sg.Window('Dados do Usuario').layout(layout)
        # Extrair os dados da tela
        self.button, self.value = janela.Read()
    def Iniciar(self):
        nome = self.value['nome']
        idade = self.value['idade']
        print(f'nome: {nome}, idade: {idade} ')

    def email(self):
        if (self.value['gmail'] == True):
                print('Usa email')
        if (self.value['outlook'] == True):
                print('Usa outlook')
        if (self.value['yahoo'] == True):
                print('Usa yahoo')


tela = TelaPython()
tela.Iniciar()
tela.email()