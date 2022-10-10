import speech_recognition as sr


def identificar_microfones():
    for indice, nome in enumerate(sr.Microphone.list_microphone_names()):
        print(f'Índice: {indice} = Microfone - {nome}')


def fone_de_ouvido():
    microfone = 0
    for indice, nome in enumerate(sr.Microphone.list_microphone_names()):
        if nome == 'Headset (i12 Hands-Free AG Audi':
            microfone = indice
            break
    return microfone


def escutar(microfone=0, fone=True):
    rec = sr.Recognizer()

    indice = microfone
    if fone:
        indice = fone_de_ouvido()

    with sr.Microphone(device_index=indice) as mic:
        rec.adjust_for_ambient_noise(mic)
        print('Ao seu dispor, senhor!')

        audio = rec.listen(mic)
        txt = rec.recognize_google(audio, language='pt-BR')
        return txt
