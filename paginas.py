"""Páginas do livro"""
import os
import time


def texto(numero):
    import logica
    logica.apagar()
    numero = str(numero)
    with open(r'txt\pagina ' + numero + '.txt', 'r', encoding='utf-8') as \
            pagina:
        pagina = pagina.read()
        for letra in pagina:
            time.sleep(0.0)  # todo tempo zerado para teste
            print(letra, end='', flush=True)
    os.system('pause')
    return
