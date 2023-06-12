import PySimpleGUI as sg
import love as lv
import time

# Definindo o layout da tela
layout = [
    [sg.Text("Bem-vindo à Minha Tela")],
    [sg.Button("Clique Aqui")],
    [sg.Button("Love")],

    [sg.Button("Sair")]
]

# Criando a janela
window = sg.Window("Minha Tela", layout, resizable=True)

# Loop principal de eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    elif event == "Clique Aqui":
        sg.popup("Você clicou no botão!")        
    elif event == "Love":
        lv.love()
        time.sleep(5)


# Fechando a janela ao sair do loop
window.close()
