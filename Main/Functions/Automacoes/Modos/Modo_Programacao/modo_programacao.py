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

# Abre o Visual Studio Code
abrir('Visual Studio Code')

# Abre o Google Chrome
abrir('Google Chrome')

# Abre o Github
pesquisar('github.com/alunogmfs2')

# Abre o Gthub Desktop
abrir('GitHub Desktop')
