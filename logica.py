"""
- Arquivo para a lógica de funcionamento do livro;
- Deverá conter as chamadas das funções das páginas;
- Fornecer uma resposta para o usuário conforme suas interações;
"""
import os
import paginas

from colorama import Fore


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
    interacao = input("\nSe você deseja ir atrás do guarda escreva:"
                      + Fore.GREEN + " Seguir\n\n" + Fore.RESET
                      + "Se você deseja espiar atrás da cortina escreva:"
                      + Fore.YELLOW + " Espiar\n" + Fore.RESET)
    interacao = interacao.lower()

    if interacao == 'seguir':
        # Caminho Concluído
        caminho_01()
    else:
        # Caminho concluído
        caminho_02()
    return


# Caminho concluído
def caminho_01():
    paginas.texto(5)
    paginas.texto(6)
    paginas.texto(8)
    interacao = input("\nSe você for chamar a polícia, escreva:"
                      + Fore.RED + " Policia\n\n" + Fore.RESET
                      + "Se você resolver perseguir o Farrel, escreva:"
                      + Fore.GREEN + " Seguir\n" + Fore.RESET)
    interacao = interacao.lower()
    if interacao == 'policia':
        # Caminho concluído
        caminho_03()
    else:
        # Caminho concluído
        caminho_04()
    return


def caminho_02():
    paginas.texto(19)
    interacao = input('\nSe você deseja ficar digite,'
                      + Fore.RED + 'ficar\n\n' + Fore.RESET
                      + 'Se você deseja sair digite,'
                      + Fore.GREEN + 'sair\n' + Fore.RESET)
    interacao = interacao.lower()
    if interacao == 'ficar':
        # Caminho concluído
        caminho_19()
    else:
        # Caminho concluído
        caminho_20()
    return


def caminho_03():
    paginas.texto(34)
    paginas.texto(35)
    interacao = input('\nSe você deseja mostrar o bilhete para Dona Teca, '
                      'digite: Mostrar\n\n'
                      'Se você quer guardar segredo, digite: segredo\n')
    interacao = interacao.lower()
    if interacao == 'mostrar':
        # Caminho concluído
        caminho_07()
    else:
        # Caminho concluído
        caminho_08()
    return


# Caminho concluído
def caminho_04():
    paginas.texto(14)
    paginas.texto(15)
    interacao = input('\nSe você deseja perseguir Farrel, digite: Seguir\n\n'
                      'Se você deseja ajudar o velho, digite: Ajudar\n')
    interacao = interacao.lower()

    if interacao == 'seguir':
        # Caminho concluído
        caminho_05()
    else:
        # Caminho concluído
        caminho_06()
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
    interacao = input('\nPegue uma moeda e jogue para o alto e agarre ela e'
                      'veja o resultado\n\nDeu cara ou coroa?\n')
    interacao = interacao.lower()

    if interacao == 'cara':
        # Caminho concluído
        caminho_09()
    else:
        # Caminho concluído
        caminho_10()
    return


def caminho_09():
    paginas.texto(44)
    paginas.texto(45)
    paginas.texto(46)
    intercao = input('\nVocê decide deixar suas coisa e ir atrás do homem '
                     'alto? digite, deixar\n\nVocê decide recolher suas '
                     'coisas? digite, recolher\n')
    intercao = intercao.lower()
    if intercao == 'deixar':
        # Caminho concluído
        caminho_11()
    else:
        # Caminho concluído
        caminho_12()
    return


def caminho_10():
    paginas.texto(9)
    interacao = input('\nSe quiser abrir digite sim, de quiser deixar fechada '
                      'digite não.')
    interacao = interacao.lower()
    if interacao == 'sim':
        # Caminho concluído
        caminho_15()
    else:
        # Caminho concluído
        caminho_16()
    return


# Caminho concluído
def caminho_11():
    paginas.texto(13)
    interacao = input('\nO primeiro desenho é a cruz Egípcia\nO '
                      'segundo é o urubu\n Qual você escolhe? Cruz ou '
                      'Urubu.\n')
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
    interacao = input('\nSe você chegou no tesouro digite, tesouro.\n'
                      'Se você chegou no beco sem saída digite, beco.\n')
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
    interacao = input('\nSe você deseja continuar correndo, digite: correr\n'
                      'Se você deseja ver quem está de seguindo, digite: '
                      'Olhar\n')
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
    interacao = input('\nSe você acha que vai ser ouvido, digite: Sim\n'
                      'Se você acha que não vai ser ouvido, Digite: Não\n')
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
