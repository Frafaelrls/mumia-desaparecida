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
            interacao = input("\nSe você deseja ir atrás do guarda escreva:"
                              + Cores.verde + " Seguir\n\n" + Cores.reset
                              + "Se você deseja espiar atrás da cortina "
                                "escreva:"
                              + Cores.vermelho + " Espiar\n" + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'seguir':
                # Caminho Concluído
                caminho_01()
                break
            elif interacao == 'espiar':
                # Caminho concluído
                caminho_02()
                break
            else:
                print(f'Você escolheu "{interacao}", esse não é um '
                      f'caminho valido :(\n'
                      f'Digite um caminho válido, escolha entre seguir ou '
                      f'espiar\n')
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
            interacao = input("\nSe você for chamar a polícia, escreva:"
                              + Cores.vermelho + " Polícia\n\n" + Cores.reset
                              + "Se você resolver perseguir o Farrel, escreva:"
                              + Cores.verde + " Seguir\n" + Cores.reset)
            interacao = interacao.lower()
            if interacao == 'policia' or interacao == 'polícia':
                # Caminho concluído
                caminho_03()
                break
            elif interacao == 'seguir':
                # Caminho concluído
                caminho_04()
                break
            else:
                print(f'Você escolheu "{interacao}", esse não é um '
                      f'caminho valido :(\n'
                      f'Digite um caminho válido, escolha entre Polícia ou '
                      f'Seguir\n')
                continue
        except ValueError:
            print('Erro')
            break
    return


def caminho_02():
    paginas.texto(19)
    while True:
        try:
            interacao = input('\nSe você deseja ficar digite,'
                              + Cores.vermelho + 'Ficar\n\n' + Cores.reset
                              + 'Se você deseja sair digite,'
                              + Cores.verde + 'Sair\n' + Cores.reset)
            interacao = interacao.lower()
            if interacao == 'ficar':
                # Caminho concluído
                caminho_19()
                break
            elif interacao == 'sair':
                # Caminho concluído
                caminho_20()
                break
            else:
                print(f'Você escolheu "{interacao}", esse não é um '
                      f'caminho valido :(\n'
                      f'Digite um caminho válido, escolha entre Ficar ou '
                      f'Sair\n')
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
                              'Teca, digite:'
                              + Cores.verde + ' Mostrar\n\n' + Cores.reset
                              + 'Se você quer guardar segredo, digite:'
                              + Cores.vermelho + ' Segredo\n' + Cores.reset)
            interacao = interacao.lower()
            if interacao == 'mostrar':
                # Caminho concluído
                caminho_07()
                break
            elif interacao == 'segredo':
                # Caminho concluído
                caminho_08()
                break
            else:
                print(f'Você escolheu "{interacao}", esse não é um '
                      f'caminho valido :(\n'
                      f'Digite um caminho válido, escolha entre Mostrar ou '
                      f'Segredo\n')
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
            interacao = input('\nSe você deseja perseguir Farrel, digite: '
                              + Cores.verde + 'Seguir\n\n' + Cores.reset
                              + 'Se você deseja ajudar o velho, digite: '
                              + Cores.vermelho + 'Ajudar\n' + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'seguir':
                # Caminho concluído
                caminho_05()
                break
            elif interacao == 'ajudar':
                # Caminho concluído
                caminho_06()
                break
            else:
                print(f'Você escolheu "{interacao}", esse não é um '
                      f'caminho valido :(\n'
                      f'Digite um caminho válido, escolha entre Seguir ou '
                      f'Ajudar\n')
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
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_06():
    paginas.texto(20)
    paginas.texto(21)
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_07():
    paginas.texto(10)
    paginas.texto(12)
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


def caminho_08():
    paginas.texto(41)
    while True:
        try:
            interacao = input('\nPegue uma moeda e jogue para o alto e agarre '
                              'ela e veja o resultado\n\nDeu '
                              + Cores.vermelho + 'cara ' + Cores.reset
                              + 'ou'
                              + Cores.verde + ' coroa?\n' + Cores.reset)
            interacao = interacao.lower()

            if interacao == 'cara':
                # Caminho concluído
                caminho_09()
                break
            elif interacao == 'coroa':
                # Caminho concluído
                caminho_10()
                break
            else:
                print(f'Você escolheu "{interacao}", esse não é um '
                      f'caminho valido :(\n'
                      f'Digite um caminho válido, escolha entre Cara ou '
                      f'Coroa\n')
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
                              'homem alto? digite, '
                              + Cores.verde + 'deixar\n\n' + Cores.reset
                              + 'Você decide recolher suas coisas? digite, '
                              + Cores.vermelho + 'recolher\n' + Cores.reset)
            interacao = interacao.lower()
            if interacao == 'deixar':
                # Caminho concluído
                caminho_11()
                break
            elif interacao == 'recolher':
                # Caminho concluído
                caminho_12()
                break
            else:
                print(f'Você escolheu "{interacao}", esse não é um '
                      f'caminho valido :(\n'
                      f'Digite um caminho válido, escolha entre Deixar ou '
                      f'Recolher\n')
                continue
        except ValueError:
            print('Erro')
            break
    return


def caminho_10():
    paginas.texto(9)
    while True:
        try:
            interacao = input('\nSe quiser abrir digite '
                              + Cores.verde + 'sim' + Cores.reset
                              + ', se quiser deixar fechada digite '
                              + Cores.vermelho + 'não.' + Cores.reset)
            interacao = interacao.lower()
            if interacao == 'sim':
                # Caminho concluído
                caminho_15()
            elif interacao == 'não' or interacao == 'nao':
                # Caminho concluído
                caminho_16()
            else:
                print(f'Você escolheu "{interacao}", esse não é um '
                      f'caminho valido :(\n'
                      f'Digite um caminho válido, escolha entre Sim ou '
                      f'Não\n')
                continue
        except ValueError:
            print('Erro')
            break
    return


# Caminho concluído
def caminho_11():
    paginas.texto(13)
    interacao = input('\nO primeiro desenho é a cruz Egípcia\nO '
                      'segundo é o urubu\n Qual você escolhe? '
                      + Cores.vermelho + 'Cruz ' + Cores.reset
                      + 'ou '
                      + Cores.verde + 'Urubu.\n' + Cores.reset)
    interacao = interacao.lower()
    if interacao == 'cruz':
        # Caminho concluído
        caminho_13()
    else:
        # Caminho concluído
        caminho_14()


# Caminho concluído
def caminho_12():
    paginas.texto(52)
    paginas.texto(53)
    paginas.texto(54)
    paginas.texto(56)
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_13():
    paginas.texto(39)
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_14():
    paginas.texto(22)
    paginas.texto(23)
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_15():
    paginas.texto(16)
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_16():
    paginas.texto(24)
    print('\n')
    paginas.texto(25)
    paginas.texto(58)
    interacao = input('\nSe você chegou no tesouro digite, '
                      + Cores.vermelho + 'tesouro.\n' + Cores.reset
                      + 'Se você chegou no beco sem saída digite, '
                      + Cores.verde + 'beco.\n' + Cores.reset)
    interacao = interacao.lower()

    if interacao == 'tesouro':
        # Caminho concluído
        caminho_17()
    else:
        # Caminho concluído
        caminho_18()
    return


# Caminho concluído
def caminho_17():
    paginas.texto(31)
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_18():
    paginas.texto(36)
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_19():
    paginas.texto(4)
    paginas.texto(27)
    paginas.texto(28)
    paginas.texto(29)
    paginas.texto(30)
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


def caminho_20():
    paginas.texto(37)
    interacao = input('\nSe você deseja continuar correndo, digite: '
                      + Cores.verde + 'correr\n' + Cores.reset
                      + 'Se você deseja ver quem está de seguindo, digite: '
                      + Cores.vermelho + 'Olhar\n' + Cores.reset)
    interacao = interacao.lower()
    if interacao == 'correr':
        # Caminho concluído
        caminho_21()
    else:
        # Caminho concluído
        caminho_22()
    return


# Caminho concluído
def caminho_21():
    paginas.texto(38)
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


def caminho_22():
    paginas.texto(40)
    paginas.texto(42)
    interacao = input('\nSe você acha que vai ser ouvido, digite: '
                      + Cores.verde + 'Sim\n' + Cores.reset
                      + 'Se você acha que não vai ser ouvido, Digite: '
                      + Cores.vermelho + 'Não\n' + Cores.reset)
    interacao = interacao.lower()

    if interacao == 'sim':
        # Caminho concluído
        caminho_23()
    else:
        # Caminho concluído
        caminho_24()
    return


# Caminho concluído
def caminho_23():
    paginas.texto(48)
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_24():
    paginas.texto(49)
    paginas.texto(50)
    paginas.texto(57)
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return
