import pyttsx3

texto = "Olá, estou falando em Python!"

# Inicializa o mecanismo de síntese de voz
engine = pyttsx3.init()

# Define a velocidade de fala (opcional)
engine.setProperty('rate', 150)

# Define o texto a ser sintetizado
engine.say(texto)

# Aguarda até que a fala seja concluída
engine.runAndWait()
