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

# Abre o Fusion
abrir('Fusion')

# Abre o Google Chrome
abrir('Google Chrome')

# Abre o Youtube
pesquisar('https://www.youtube.com/ ')
