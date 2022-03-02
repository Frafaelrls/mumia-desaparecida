"""
*** Pagina 58 do livro ***

Para essa página será necessário o uso de um labirinto interativo.

O leitor deverá seguir pelo labirinto, o local onde terminar o jogo será o
local onde deverá prosseguir com a história.

todo fazer o mapa ficar com o layout igual ou próximo do livro.

todo terminar a lógica e implementar a interação com usuário.
"""
import turtle

# Criando a janela do jogo
janela = turtle.Screen()
# Adicionando nova imagem para as paredes
janela.addshape('imagens/mumia.gif')
# Definindo imagem de fundo
janela.bgpic('imagens/back.gif')
# Definindo cor de fundo
janela.bgcolor('black')
# Definindo o título da janela
janela.title('Labirinto')
# Definindo o tamanho da janela
janela.setup(700, 700)
# Bloqueando o maximizar tela
janela._root.resizable(False, False)


# Criando a classe pen, que definirá o estilo das paredes
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        # Definindo o formato
        self.shape('imagens/mumia.gif')
        # Definindo a cor
        self.color('white')
        # Definindo se a caneta vai sempre tocar a folha
        self.penup()
        # Definindo a velocidade que vai criar o labirinto
        self.speed(0)


# Criando a classe do jogador
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('blue')
        self.penup()
        self.speed(0)

# Criando uma lista de níveis todo apagar essa parte
levels = ['']

# Definindo o layout do primeiro nível
leve_01 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP   XXXXXXXXXXXXXXXXXXXX",
"X    XXXXXXXXXXXXXXXXXXXX",
"X    XXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXX     XXXXXXXXXXXX",
"XXXXXXXX     XXXXXXXXXXXX",
"XXXXXXXX     XXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXXX  XXXXXXXXXXXX",
"XXXXXXXXXXX  XXXXXXXXXXXX"
]


# Criando a definição de funcionamento do nível
def setup_maze(level):
    # todo entender os for
    while True:
        for y in range(len(level)):
            for x in range(len(level[y])):
                # Pegando as coordenadas de cada caractere
                # todo entender a ordem das de y e x na próxima linha
                character = level[y][x]
                # Calculo das coordenadas na tela
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)
                # Checando se já existe uma parede no local
                if character == 'X':
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                if character == 'P':
                    player.goto(screen_x, screen_y)
                    pen.stamp()
    

# Criando uma instância de classe todo Descobrir o que é
pen = Pen()
player = Player()
# Set up the level todo Descobrir o que é
setup_maze(leve_01)

