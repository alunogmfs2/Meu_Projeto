import pyautogui as pag
import webbrowser as wb

youtube_url = 'https://youtube.com/ '
github_url = 'https://github.com/alunogmfs2 '
windows_b = 'winleft'

pag.PAUSE = 0.5

modos_l = ['Normal', 'Python', 'Minecraft', '3d']

def abrir_youtube():
    wb.open(youtube_url)


def modo_normal():
    abrir_youtube()


def modo_python():
    pag.press(windows_b)
    pag.write('visual studio code')
    pag.press('enter')

    wb.open(youtube_url)
    wb.open(github_url)
    pag.hotkey('ctrlleft', '1')


def modo_minecraft():
    pag.press(windows_b)
    pag.write('curseforge')
    pag.press('enter')

    wb.open(youtube_url)
    wb.open('https://www.chunkbase.com/apps/seed-map ')
    pag.hotkey('ctrlleft', '1')

def modo_3d():
    pag.press(windows_b)
    pag.write('fusion')
    pag.press('enter')

    wb.open(youtube_url)
