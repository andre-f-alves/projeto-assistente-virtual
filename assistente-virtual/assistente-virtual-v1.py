import microfone as mic
import pyautogui as pg

""" 
    * No momento, a utilização do assistente está limitada a inicialização de alguns programas
    por meio da ferramenta Executar do sistema operacional Windows.
"""

pg.PAUSE = 1 # -> Define o tempo de espera entre a execução de tarefas automáticas (1s).

programas = {
    'word': 'winword',
    'excel': 'excel',
    'powerpoint': 'powerpnt',
    'onenote': 'onenote',
    'edge': 'msedge',
    'chrome': 'chrome'
}

""" 
    Ativa o microfone para a captura do áudio e divide o texto retornado,
    transformando-o em uma lista (list()).
"""
user = mic.escutar()
txtlist = str(user).lower().split(' ')
print(txtlist)

comando = ''
for palavra in txtlist:
    """
    Percorre todas as palavras da lista criada, verificando se alguma
    se encontra no dicionário 'programas' (dict()).
    """
    if palavra in programas:
        comando = palavra
        break

"""
    De forma automática, abre o Executar, indica o programa que será iniciado
    por meio do comando definido em 'programas' e pressiona Enter para iniciá-lo.
"""
pg.hotkey('win', 'r')
pg.write(programas[comando])
pg.press('enter')
