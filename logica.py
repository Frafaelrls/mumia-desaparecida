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
    escolha = input(f"Se você deseja ir atrás do guarda escreva: seguir\n\n"
                    f"Se você deseja espiar atrás da cortina escreva: "
                    f"espiar\n")
    escolha = escolha.lower()
    if escolha == 'seguir':
        apagar()
        paginas.pagina_05()
    else:
        apagar()
        paginas.pagina_19()


