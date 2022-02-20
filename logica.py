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
    paginas.pagina_01()
    paginas.pagina_02()
    paginas.pagina_03()
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
    paginas.pagina_05()
    paginas.pagina_06()
    paginas.pagina_08()
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
    paginas.pagina_19()
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
    paginas.pagina_34()
    paginas.pagina_35()
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
    paginas.pagina_14()
    paginas.pagina_15()
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
    paginas.pagina_43()
    paginas.pagina_32()
    paginas.pagina_33()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_06():
    paginas.pagina_20()
    paginas.pagina_21()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_07():
    paginas.pagina_10()
    paginas.pagina_12()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


def caminho_08():
    paginas.pagina_41()
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
    paginas.pagina_44()
    paginas.pagina_45()
    paginas.pagina_46()
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
    paginas.pagina_09()
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
    paginas.pagina_13()
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
    paginas.pagina_52()
    paginas.pagina_53()
    paginas.pagina_54()
    paginas.pagina_56()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_13():
    paginas.pagina_39()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_14():
    paginas.pagina_22()
    paginas.pagina_23()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_15():
    paginas.pagina_16()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_16():
    paginas.pagina_24()
    print('\n')
    paginas.pagina_25()
    paginas.pagina_58()
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
    paginas.pagina_31()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_18():
    paginas.pagina_36()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_19():
    paginas.pagina_04()
    paginas.pagina_27()
    paginas.pagina_28()
    paginas.pagina_29()
    paginas.pagina_30()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


def caminho_20():
    paginas.pagina_37()
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
    paginas.pagina_38()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


def caminho_22():
    paginas.pagina_40()
    paginas.pagina_42()
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
    paginas.pagina_48()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_24():
    paginas.pagina_49()
    paginas.pagina_50()
    paginas.pagina_57()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return
