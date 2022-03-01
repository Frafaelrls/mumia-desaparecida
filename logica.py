"""
- Arquivo para a lógica de funcionamento do livro;
- Deverá conter as chamadas das funções das páginas;
- Fornecer uma resposta para o usuário conforme suas interações;
"""
import os

import colorama

import paginas
# Biblioteca colorama não é nativa do sistema
# Funciona apenas com versão igual o inferior a 3,8


class Cores:
    colorama.init()
    vermelho = '\033[1;31m'
    verde = '\033[1;32m'
    negrito = '\033[;1m'
    reset = '\033[0;0m'


# Função para limpar o terminal
def apagar():
    # Se mac ou linux
    limpar = "clear"
    # Se Windows
    if os.name in ("nt", "dos"):
        os.system('cls')
    else:
        os.system(limpar)
    return


def leitura():
    paginas.texto(1)
    paginas.texto(2)
    paginas.texto(3)
    while True:
        try:
            interacao = input("\nSe você deseja ir atrás do guarda escreva:" +
                              Cores.verde + " Seguir\n\n" + Cores.reset +
                              "Se você deseja espiar atrás da cortina "
                              "escreva:" +
                              Cores.vermelho + " Espiar\n\n" + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'seguir':
                # Caminho Concluído
                caminho_01()
                break
            elif interacao == 'espiar':
                # Caminho concluído
                caminho_02()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


# Caminho concluído
def caminho_01():
    paginas.texto(5)
    paginas.texto(6)
    paginas.texto(8)
    while True:
        try:
            interacao = input("\nSe você for chamar a polícia, escreva:" +
                              Cores.vermelho + " Polícia\n\n" + Cores.reset +
                              "Se você resolver perseguir o Farrel, escreva:" +
                              Cores.verde + " Seguir\n\n" + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'policia' or interacao == 'polícia':
                # Caminho concluído
                caminho_03()
                break
            elif interacao == 'seguir':
                # Caminho concluído
                caminho_04()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


def caminho_02():
    paginas.texto(19)
    while True:
        try:
            interacao = input('\nSe você deseja ficar digite,' +
                              Cores.vermelho + ' ficar\n\n' + Cores.reset +
                              'Se você deseja sair digite,' +
                              Cores.verde + ' sair\n\n' + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'ficar':
                # Caminho concluído
                caminho_19()
                break
            elif interacao == 'sair':
                # Caminho concluído
                caminho_20()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


def caminho_03():
    paginas.texto(34)
    paginas.texto(35)
    while True:
        try:
            interacao = input('\nSe você deseja mostrar o bilhete para Dona '
                              'Teca, digite:' +
                              Cores.verde + ' Mostrar\n\n' + Cores.reset +
                              'Se você quer guardar segredo, digite:' +
                              Cores.vermelho + ' Segredo\n\n' + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'mostrar':
                # Caminho concluído
                caminho_07()
                break
            elif interacao == 'segredo':
                # Caminho concluído
                caminho_08()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


# Caminho concluído
def caminho_04():
    paginas.texto(14)
    paginas.texto(15)
    while True:
        try:
            interacao = input('\nSe você deseja perseguir Farrel, digite: ' +
                              Cores.verde + 'Seguir\n\n' + Cores.reset +
                              'Se você deseja ajudar o velho, digite: ' +
                              Cores.vermelho + 'Ajudar\n\n' + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'seguir':
                # Caminho concluído
                caminho_05()
                break
            elif interacao == 'ajudar':
                # Caminho concluído
                caminho_06()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


# Caminho concluído
def caminho_05():
    paginas.texto(43)
    paginas.texto(32)
    paginas.texto(33)
    final()
    return


# Caminho concluído
def caminho_06():
    paginas.texto(20)
    paginas.texto(21)
    final()
    return


# Caminho concluído
def caminho_07():
    paginas.texto(10)
    paginas.texto(12)
    final()
    return


def caminho_08():
    paginas.texto(41)
    while True:
        try:
            interacao = input('\nPegue uma moeda e jogue para o alto e agarre '
                              'ela e veja o resultado\n\nDeu ' +
                              Cores.vermelho + 'cara ' + Cores.reset +
                              'ou' +
                              Cores.verde + ' coroa?\n\n' + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'cara':
                # Caminho concluído
                caminho_09()
                break
            elif interacao == 'coroa':
                # Caminho concluído
                caminho_10()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


def caminho_09():
    paginas.texto(44)
    paginas.texto(45)
    paginas.texto(46)
    while True:
        try:
            interacao = input('\nVocê decide deixar suas coisa e ir atrás do '
                              'homem alto? digite, ' +
                              Cores.verde + 'deixar\n\n' + Cores.reset +
                              'Você decide recolher suas coisas? digite, ' +
                              Cores.vermelho + 'recolher\n\n' + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'deixar':
                # Caminho concluído
                caminho_11()
                break
            elif interacao == 'recolher':
                # Caminho concluído
                caminho_12()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


def caminho_10():
    paginas.texto(9)
    while True:
        try:
            interacao = input('\nSe quiser abrir digite ' +
                              Cores.verde + 'sim' + Cores.reset +
                              ', se quiser deixar fechada digite ' +
                              Cores.vermelho + 'não.\n\n' + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'sim':
                # Caminho concluído
                caminho_15()
                break
            elif interacao == 'não' or interacao == 'nao':
                # Caminho concluído
                caminho_16()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


# Caminho concluído
def caminho_11():
    paginas.texto(13)
    while True:
        try:
            interacao = input('\nO primeiro desenho é a cruz Egípcia\n'
                              'O segundo é o urubu\n Qual você escolhe? ' +
                              Cores.vermelho + 'Cruz ' + Cores.reset +
                              'ou ' +
                              Cores.verde + 'Urubu.\n\n' + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'cruz':
                # Caminho concluído
                caminho_13()
                break
            elif interacao == 'urubu':
                # Caminho concluído
                caminho_14()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


# Caminho concluído
def caminho_12():
    paginas.texto(52)
    paginas.texto(53)
    paginas.texto(54)
    paginas.texto(56)
    final()
    return


# Caminho concluído
def caminho_13():
    paginas.texto(39)
    final()
    return


# Caminho concluído
def caminho_14():
    paginas.texto(22)
    paginas.texto(23)
    final()
    return


# Caminho concluído
def caminho_15():
    paginas.texto(16)
    final()
    return


# Caminho concluído
def caminho_16():
    paginas.texto(24)
    paginas.texto(25)
    paginas.texto(58)
    while True:
        try:
            interacao = input('\nSe você chegou no tesouro digite, ' +
                              Cores.vermelho + 'tesouro.\n\n' + Cores.reset +
                              'Se você chegou no beco sem saída digite, ' +
                              Cores.verde + 'beco.\n\n' + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'tesouro':
                # Caminho concluído
                caminho_17()
                break
            elif interacao == 'beco':
                # Caminho concluído
                caminho_18()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


# Caminho concluído
def caminho_17():
    paginas.texto(31)
    final()
    return


# Caminho concluído
def caminho_18():
    paginas.texto(36)
    final()
    return


# Caminho concluído
def caminho_19():
    paginas.texto(4)
    paginas.texto(27)
    paginas.texto(28)
    paginas.texto(29)
    paginas.texto(30)
    final()
    return


def caminho_20():
    paginas.texto(37)
    while True:
        try:
            interacao = input('\nSe você deseja continuar correndo, digite: ' +
                              Cores.verde + 'Correr\n\n' + Cores.reset +
                              'Se você deseja ver quem está de seguindo, ' 
                              'digite: ' +
                              Cores.vermelho + 'Olhar\n\n' + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'correr':
                # Caminho concluído
                caminho_21()
                break
            elif interacao == 'olhar':
                # Caminho concluído
                caminho_22()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


# Caminho concluído
def caminho_21():
    paginas.texto(38)
    final()
    return


def caminho_22():
    paginas.texto(40)
    paginas.texto(42)
    while True:
        try:
            interacao = input('\nSe você acha que vai ser ouvido, digite: ' +
                              Cores.verde + 'Sim\n\n' + Cores.reset +
                              'Se você acha que não vai ser ouvido, Digite:' +
                              Cores.vermelho + ' Não\n\n' + Cores.reset +
                              "Caso queira terminar a leitura escreva: " +
                              Cores.vermelho + "Exit\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'sim':
                # Caminho concluído
                caminho_23()
                break
            elif interacao == 'não' or interacao == 'nao':
                # Caminho concluído
                caminho_24()
                break
            elif interacao == 'exit':
                saida()
                break
            else:
                caminho_invalido(interacao)
                continue
        except ValueError:
            print('Erro')
            break
    return


# Caminho concluído
def caminho_23():
    paginas.texto(48)
    final()
    return


# Caminho concluído
def caminho_24():
    paginas.texto(49)
    paginas.texto(50)
    paginas.texto(57)
    final()
    return


def saida():
    print('Esperamos você em um outro momento, até breve :)')
    os.system('pause')


def caminho_invalido(interacao):
    apagar()
    print('Você escolheu ' + Cores.vermelho + f'"{interacao}"' + Cores.reset +
          ',esse não é um caminho válido :(\nDigite um caminho válido.')


def final():
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
