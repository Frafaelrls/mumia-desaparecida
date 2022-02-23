"""Páginas do livro"""
import os
import time


def paginas(numero):
    import logica
    logica.apagar()
    print(f"Texto da página {numero}")
    numero = str(numero)
    with open(r'txt\pagina ' + numero + '.txt', 'r', encoding='utf-8') as \
            pagina:
        pagina = pagina.read()
        for letra in pagina:
            time.sleep(0.0)  # todo tempo zerado para teste
            print(letra, end='', flush=True)
    os.system('pause')
    return
