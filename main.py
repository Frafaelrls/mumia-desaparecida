import time
import os
import paginas

introducao = "O mistério da Múmia Desaparecida\n\n" \
         "Você está prestes a iniciar a leitura de um livro " \
         "interativo.\nSaiba que suas escolhas trarão consequências.\nVocê " \
         "possui nível suficiente para essa aventura?\n\n"\
         "Digite Sim para iniciar, digite Não se precisar de mais XP.\n"

for letra in introducao:
    time.sleep(0.08)
    print(letra, end='', flush=True)


resposta = input()
resposta = resposta.lower()
if resposta == "sim":
    print("Que a ventura comesse.\n")
    time.sleep(0.5)
    paginas.pagina_01()
    os.system("pause")
else:
    print("Volte quando tiver mais XP\n")
    print("FECHA O LIVRO")
    os.system("pause")
