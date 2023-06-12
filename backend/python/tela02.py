import PySimpleGUI as sg

# Definindo o layout da tela
layout = [
    [sg.Text("Bem-vindo ao PySimpleGUI!")],
    [sg.Text("Digite seu nome:"), sg.Input(key="-NOME-")],
    [sg.Text("Escolha sua linguagem preferida:"), sg.Combo(["Python", "Java", "C++"], key="-LINGUAGEM-")],
    [sg.Text("Selecione seus hobbies:"), sg.Checkbox("Esportes", key="-ESPORTES-"), sg.Checkbox("Leitura", key="-LEITURA-")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
]

# Criando a janela
window = sg.Window("Exemplo PySimpleGUI", layout)

# Loop principal de eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Cancelar":
        break
    elif event == "Enviar":
        nome = values["-NOME-"]
        linguagem = values["-LINGUAGEM-"]
        esportes = values["-ESPORTES-"]
        leitura = values["-LEITURA-"]
        sg.popup(f"Nome: {nome}\nLinguagem preferida: {linguagem}\nEsportes: {esportes}\nLeitura: {leitura}")

# Fechando a janela ao sair do loop
window.close()
