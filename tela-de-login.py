import PySimpleGUI as sg

#Style das janelas
def janela_login():
     sg.theme('Reddit')
     lay = [
     [sg.Text('Usuario'), sg.Input(key='Usuario', size=(20,1))],
     [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
     [sg.Checkbox('Salvar o login?')],
     [sg.Button('Entrar')],
     ]
     return sg.Window('Login', layout=lay, finalize=True)
def janela_alerta():
     sg.theme('Reddit')
     layout = [sg.Text('Usuario nao encontrado')
    ]
     return sg.Window('Alerta', Layout=layout,finalize=True)
#Janelas inicias
janela1, janela2 = janela_login(), janela_alerta()
#Criando um loop de leitura
while True:
        window, event, values = sg.read_all_windows()
    #quando a janela for fechada
        if window == janela1 and event == sg.WINDOW_CLOSED:
            break
    #qundo ir para a proxima janela
        if window == janela1 and event == 'Entrar':
            janela2 = janela_alerta()
            janela1.hide()
             
            
