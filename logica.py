"""
- Arquivo para a lógica de funcionamento do livro;
- Deverá conter as chamadas das funções das páginas;
- Fornecer uma resposta para o usuário conforme suas interações;
"""
import os
import paginas


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
    os.system('pause')
    apagar()
    paginas.pagina_02()
    os.system('pause')
    apagar()
    paginas.pagina_03()
    os.system('pause')
    apagar()
    interacao = input("Se você deseja ir atrás do guarda escreva: Seguir\n\n"
                      "Se você deseja espiar atrás da cortina escreva: "
                      "Espiar\n")
    interacao = interacao.lower()

    if interacao == 'seguir':
        # Caminho Concluído
        caminho_01()
    else:
        caminho_02()
    return


def caminho_01():
    apagar()
    paginas.pagina_05()
    os.system('pause')
    paginas.pagina_06()
    os.system('pause')
    paginas.pagina_08()
    os.system('pause')
    interacao = input("Se você for chamar a polícia, escreva: Policia\n\n"
                      "Se você resolver perseguir o Farrel, escreva: "
                      "Seguir\n")
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
    return


def caminho_03():
    paginas.pagina_34()
    os.system('pause')
    paginas.pagina_35()
    os.system('pause')
    apagar()
    interacao = input('Se você deseja mostrar o bilhete para Dona Teca, '
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
    os.system('pause')
    paginas.pagina_15()
    os.system('pause')
    apagar()
    interacao = input('Se você deseja perseguir Farrel, digite: Seguir\n\n'
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
    os.system('pause')
    paginas.pagina_32()
    os.system('pause')
    paginas.pagina_33()
    os.system('pause')
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    apagar()
    return


# Caminho concluído
def caminho_06():
    paginas.pagina_20()
    os.system('pause')
    paginas.pagina_21()
    os.system('pause')
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    apagar()
    return


# Caminho concluído
def caminho_07():
    paginas.pagina_10()
    os.system('pause')
    paginas.pagina_12()
    os.system('pause')
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    apagar()
    return


def caminho_08():
    paginas.pagina_41()
    os.system('pause')
    apagar()
    interacao = input('Pegue uma moeda e jogue para o alto e agarre ela e'
                      'veja o resultado\nDeu cara ou coroa?\n')
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
    os.system('pause')
    paginas.pagina_45()
    os.system('pause')
    paginas.pagina_46()
    intercao = input('Você decide deixar suas coisa e ir atrás do homem '
                     'alto? digite, deixar\nVocê decide recolher suas '
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
    interacao = input('Se quiser abrir digite sim, de quiser deixar fechada '
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
    os.system('pause')
    interacao = input('O primeiro desenho é a cruz Egípcia\nO '
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
    os.system('pause')
    paginas.pagina_53()
    os.system('pause')
    paginas.pagina_54()
    os.system('pause')
    paginas.pagina_56()
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    apagar()
    return


# Caminho concluído
def caminho_13():
    paginas.pagina_39()
    os.system('pause')
    apagar()
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    apagar()
    return


# Caminho concluído
def caminho_14():
    paginas.pagina_22()
    os.system('pause')
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
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return


# Caminho concluído
def caminho_16():
    paginas.pagina_24()
    os.system('pause')
    paginas.pagina_25()
    os.system('pause')
    paginas.pagina_58()
    interacao = input('Se você chegou no tesouro digite, tesouro.\n'
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
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Reinicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
    return