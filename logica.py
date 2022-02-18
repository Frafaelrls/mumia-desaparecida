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
    interacao = input(f"Se você deseja ir atrás do guarda escreva: Seguir\n\n"
                      f"Se você deseja espiar atrás da cortina escreva: "
                      f"Espiar\n")
    interacao = interacao.lower()

    if interacao == 'seguir':
        caminho_01()
    else:
        caminho_02()
    return


def caminho_01():
    paginas.pagina_05()
    os.system('pause')
    paginas.pagina_06()
    os.system('pause')
    paginas.pagina_08()
    os.system('pause')
    interacao = input(f"Se você for chamar a polícia, escreva: Policia\n\n"
                      f"Se você resolver perseguir o Farrel, escreva: "
                      f"Seguir\n")
    interacao = interacao.lower()
    if interacao == 'policia':
        caminho_03()
    else:
        caminho_04()
    return


def caminho_02():
    paginas.pagina_19()
    return


def caminho_03():
    paginas.pagina_34()
    os.system('pause')

    return


def caminho_04():
    paginas.pagina_14()
    os.system('pause')
    paginas.pagina_15()
    os.system('pause')
    interacao = input(f'Se você deseja perseguir Farrel, digite: Seguir\n\n'
                      f'Se você deseja ajudar o velho, digite: Ajudar')
    interacao = interacao.lower()

    if interacao == 'seguir':
        caminho_05()
    else:
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
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Inicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()


# Caminho concluído
def caminho_06():
    paginas.pagina_20()
    os.system('pause')
    paginas.pagina_21()
    os.system('pause')
    print('Você chegou ao final de uma aventura esperamos que tenha gostado.\n'
          'Inicie o jogo para se aventurar com outras possibilidades.')
    os.system('pause')
    apagar()
