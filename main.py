import time
import os
import logica
from logica import Cores


titulo = Cores.negrito + 'O mistério da Múmia Desaparecida\n\n' + Cores.reset
introducao = """
Você está prestes a iniciar a leitura de um livro interativo.
Saiba que suas escolhas trarão consequências.
Você possui nível suficiente para essa aventura?
Digite Sim para iniciar, digite Não se precisar de mais XP.
"""

for letra in titulo:
    time.sleep(0.0)  # todo tempo zerado para teste
    print(letra, end='', flush=True)

for letra in introducao:
    time.sleep(0.0)  # todo tempo zerado para teste
    print(letra, end='', flush=True)

while True:
    try:
        resposta = input()
        resposta = resposta.lower()
        if resposta == "sim":
            print('Que as aventuras comecem.\n')
            time.sleep(0.0)  # todo tempo zerado para teste
            os.system('pause')
            logica.leitura()
        elif resposta == 'nao' or 'não':
            print('Volte quando tiver mais XP\n')
            print('Fechando o livro....\nAperte qualquer tecla para finalizar')
            os.system('pause >nul')
            break

        else:
            print('Digite sim para iniciar ou não para fechar o livro.')
            continue
    except ValueError:
        print('Erro')
        break
