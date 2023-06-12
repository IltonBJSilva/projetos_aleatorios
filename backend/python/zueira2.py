import pyautogui as pg
import random
import time


time.sleep(5)
'''
mensagens = [
"E aí, meu chapa!",
"Tá ligado, irmão?",
"Mano, tô suave!",
"Brother, bora marcar uma parada?",
"Eita, meu consagrado!",
"Fala tu, meu parceiro!",
"Meu chapa, você é o cara!",
"Ô meu rei, tudo tranquilo?",
"E aí, brother, tudo em cima?",
"Falou, meu chegado!",
"E aí, maluco, firmeza?",
"Salve, meu mano!",
"Eita, meu camarada, como é que tá?",
"Opa, meu chapa, beleza?",
"E aí, parceiro, tudo na paz?",
"Bro, só chego junto!",
"Meu rei, estamos junto nessa!",
"Fala aí, meu camarada, qual é a parada?",
"Eita, meu brother, bora curtir!",
"Fala, meu chegado, tamo junto!",
"E aí, malandragem, tá suave?",
"Ô meu chapa, tô na área!",
"E aí, brother, tudo tranquilo na quebrada?",
"Salve, salve, meu parceiro!",
"Eita, meu camarada, bora desenrolar?",
"Fala tu, meu chapa, bora trocar uma ideia?",
"Meu brother, bora fazer acontecer!",
"Ô meu chegado, tô na correria!",
"E aí, maluco, tá tudo beleza?"]
'''


mensagens = [
"E aí, firmeza?",
"Vamo bater um rango?",
"Cara, tô de boa!",
"Mermão, cê tá ligado?",
"Qual é a boa, meu parceiro?",
"Ô meu, tá trampando muito?",
"Bora pro rolê?",
"Tá no corre, meu chapa!",
"Véi, cê tá bolado?",
"Eita, tá suave?",
"Mano, vamo marcar um rolêzinho?",
"E aí, truta, tudo beleza?",
"Mermão, cê é zica!",
"Ô meu, tô na correria!",
"Bora curtir uma balada?",
"Cara, tu é brabo!",
"E aí, meu camarada, qual é a situação?",
"Véi, tá sussa?",
"Ô meu, só chega junto!",
"Bora descolar um trampo?",
"E aí, meu chapa, tudo certo?",
"Vamo colar no rolê?",
"Mano, tu é sangue bom!",
"Eita, tá no fluxo?",
"Ô meu, tá no pique?",
"Cara, cê é zueiro demais!",
"E aí, truta, bora mandar um salve?",
"Mermão, cê é arretado!",
"Véi, tá no bagulho?",
"Ô meu, tamo na atividade!"]

pg.typewrite("*"*50)
pg.typewrite("*ZueiraBot com girias paulistas*")
pg.typewrite("\n")

for i in range(50):
    msg = random.choice(mensagens)
    pg.typewrite(msg)
    pg.press('enter')












