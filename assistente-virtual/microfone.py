import speech_recognition as sr


def identificar_microfones():
    """ 
    Exibe uma lista dos microfones conectados à máquina.
    """
    for indice, nome in enumerate(sr.Microphone.list_microphone_names()):
        """ 
        Percorre a lista de microfones conectados, exibindo seu índice
        (passado para a função 'escutar()', indicando qual microfone será utilizado) e o nome.
        """
        print(f'Índice: {indice} = Microfone - {nome}')


def escutar(microfone=0):
    """ 
    Realiza o reconhecimento da fala por meio da captura do áudio do microfone
    e da remoção de ruídos de fundo, utilizando a biblioteca Speech Recognition.
    Depois, transforma o áudio capturado em texto com a ferramenta de reconhecimento do Google.
    
    Parêmtros
    =-=-=-=-=-=-=
    microfone: indica o índice do microfone conectado que será utilizado.
    
    '''
    Retorno
    =-=-=-=-=-=-=
    Retorna o áudio em formato de texto.
    """
    rec = sr.Recognizer()
    
    indice = microfone
    with sr.Microphone(device_index=indice) as mic:
        """ 
        Declara uma variável, uma forma abreviada, para utilizar o microfone indicado.
        Com isso, inicializa a captura do áudio, ajusta-o e o transforma em texto.
        No final do blocoo de código, desliga o microfone e retorna o texto.
        """
        rec.adjust_for_ambient_noise(mic)
        print('Ao seu dispor, senhor!')

        audio = rec.listen(mic)
        txt = rec.recognize_google(audio, language='pt-BR')
        return txt
