import microfone as mic
import pyautogui as pg

pg.PAUSE = 1

programas = {
    'word': 'winword',
    'excel': 'excel',
    'powerpoint': 'powerpnt',
    'onenote': 'onenote',
    'edge': 'msedge',
    'chrome': 'chrome'
}
user = mic.escutar()
txtlist = str(user).lower().split(' ')
print(txtlist)

comando = ''
for palavra in txtlist:
    if palavra in programas:
        comando = palavra
        break

pg.hotkey('win', 'r')
pg.write(programas[comando])
pg.press('enter')
