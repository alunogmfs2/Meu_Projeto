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

def nova_aba():
    pg.hotkey('ctrl', 't')
    pg.sleep(0.2)


# Abre o Roblox
abrir('Roblox')

# Abre o Google Chrome
abrir('Google Chrome')

# Abre o YouTube
pesquisar('https://www.youtube.com/ ')

# Abre uma nova aba
nova_aba()

# Abre o Roblox
pesquisar('https://www.roblox.com/home ')
