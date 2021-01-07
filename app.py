import pywhatkit
import keyboard
import time
from datetime import datetime

#Adicionar número de telefone desejado com código de área e do país
contatos = ['', '']

while len(contatos) >=1:
    pywhatkit.sendwhatmsg(contatos[0], 'Essa mensagem é um tesde de BOT. Feliz Ano novo! ', datetime.now().hour,datetime.now().minute +2)

    del contatos [0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
