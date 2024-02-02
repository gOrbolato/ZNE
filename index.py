import pyautogui as py
import random
import time

time.sleep(5)
# Abra a conversa com a pessoa desejada (isso pode variar dependendo do aplicativo)
# Exemplo: clicar na barra de pesquisa e digitar o número
# Certifique-se de ajustar esses passos de acordo com a interface do aplicativo que você está usando

# Agora, você pode enviar mensagens para a pessoa desejada
mensagens = ['MARMOTA', 'BORBOLETA PARAGUAIA']
for i in range(100):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press('enter')