import time
import os
import logica


titulo = "O mistério da Múmia Desaparecida\n"
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


resposta = input()
resposta = resposta.lower()
if resposta == "sim":
    print("Que as aventuras comecem.\n")
    time.sleep(0.0)  # todo tempo zerado para teste
    os.system("pause")
    logica.leitura()
else:
    print("Volte quando tiver mais XP\n")
    print("FECHA O LIVRO")
    os.system("pause")
