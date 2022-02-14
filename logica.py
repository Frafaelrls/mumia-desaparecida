"""
- Arquivo para a lógica de funcionamento do livro;
- Deverá conter as chamadas das funções das páginas;
- Fornecer uma resposta para o usuário conforme suas interações;
"""
import os


# Função para limpar o terminal
def apagar():
    limpar = "clear"  # Se for mac ou linux
    if os.name in ("nt", "dos"):  # Se for windows
        os.system('cls')
    else:
        os.system(limpar)
