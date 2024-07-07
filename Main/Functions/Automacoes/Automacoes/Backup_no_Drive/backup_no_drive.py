import pyautogui as pg

pg.PAUSE = 0.4

def abrir(nome_app):
    pg.press('winleft')
    pg.typewrite(nome_app)
    enter()
    pg.sleep(1)

escrever = pg.typewrite

def pesquisar(texto):
    escrever(texto)
    enter()
    pg.sleep(1)

def enter():
    pg.press('enter')

# Abre o Google Chrome
abrir('Google Chrome')

# Abre o Google Drive
pesquisar('https://drive.google.com/ ')

# Vai na Area de Trabalho
pg.hotkey('winleft', 'd')

# Vai no Arquivo
pg.moveTo(1875, 34)

# Arrasta o arquivo
pg.mouseDown()

# Vai no lugar
pg.moveTo(1122, 762)

# Vai no Google Drive
pg.hotkey('winleft', 'tab')
enter()
pg.sleep(0.5)

# Solta o arquivo
pg.mouseUp()
pg.sleep(5)

# Fecha o Google Drive
pg.hotkey('altleft', 'f4')
