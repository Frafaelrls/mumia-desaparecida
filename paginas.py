"""Páginas do livro"""
import os
import time


def pagina_01():
    import logica
    logica.apagar()
    print(f"Texto da página 01")
    with open(r'txt\pagina 01.txt', 'r', encoding='utf-8') as pagina_01X:
        pagina = pagina_01X.read()
        for palavra in pagina:
            time.sleep(0.0)  # todo tempo zerado para teste
            print(palavra, end='', flush=True)
    os.system('pause')
    return
