import os
import time

import logica

titulo = 'O mistério da Múmia Desaparecida\n\n'
introducao = """
Você está prestes a iniciar a leitura de um livro interativo.
Saiba que suas escolhas trarão consequências.

Você possui nível suficiente para essa aventura?

Digite Sim para iniciar, digite Não se precisar de mais XP.
"""

for letra in titulo:
    time.sleep(0.0)  # todo tempo zerado para teste
    print(logica.Cores.vermelho + letra + logica.Cores.reset, end='',
          flush=True)

for letra in introducao:
    time.sleep(0.0)  # todo tempo zerado para teste
    print(letra, end='', flush=True)

while True:
    try:
        resposta = input()
        resposta = resposta.lower()
        if resposta == "sim":
            print('Você poderá sair apenas quando for escolher um caminho, '
                  'basta digitar:' +
                  logica.Cores.vermelho + ' Exit' + logica.Cores.reset +
                  '\n\nQue as aventuras comecem.\n')
            os.system('pause')
            logica.leitura()
            break
        elif resposta == 'nao' or resposta == 'não':
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
