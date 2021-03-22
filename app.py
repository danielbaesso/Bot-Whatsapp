import pywhatkit
import keyboard
import time
from datetime import datetime

#Add desired phone number with country and area code between ''
contatos = ['', '']

while len(contatos) >=1:
    pywhatkit.sendwhatmsg(contatos[0], 'Essa mensagem é um teste de BOT. Obrigado! ', datetime.now().hour,datetime.now().minute +2)

    del contatos [0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
