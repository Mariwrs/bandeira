import turtle

# Configurações iniciais
leo = turtle.Turtle()
leo.shape("turtle")
leo.pensize(3)

# Função que desenha a bandeira da China
# Movimentação para o canto antes de fazer a borda da bandeira
leo.up()
leo.goto(-300, 200)
leo.down()

# Fundo vermelho da bandeira
leo.fillcolor('red')
leo.begin_fill()
for i in range(2):
    leo.forward(600)  # Largura da bandeira
    leo.right(90)
    leo.forward(400)  # Altura da bandeira
    leo.right(90)
leo.end_fill()

# Define a cor da caneta para amarelo (para evitar bordas pretas nas estrelas)
leo.pencolor('yellow')

# Movimentação para desenhar a estrela grande
leo.up()
leo.goto(-250, 150)  # Posição da estrela grande
leo.down()
leo.fillcolor('yellow')
leo.begin_fill()
for i in range(5):
    leo.forward(100)
    leo.right(144)
leo.end_fill()

# Desenha as estrelas menores

# Primeira estrela
leo.up()
leo.goto(-150, 180)  # Posição da primeira estrela menor
leo.down()
leo.fillcolor('yellow')
leo.begin_fill()
for i in range(5):
    leo.forward(30)  # Tamanho da estrela menor
    leo.right(144)
leo.end_fill()

# Segunda estrela
leo.up()
leo.goto(-120, 140)  # Posição da segunda estrela menor
leo.down()
leo.fillcolor('yellow')
leo.begin_fill()
for i in range(5):
    leo.forward(30)
    leo.right(144)
leo.end_fill()

# Terceira estrela
leo.up()
leo.goto(-120, 90)  # Posição da terceira estrela menor
leo.down()
leo.fillcolor('yellow')
leo.begin_fill()
for i in range(5):
    leo.forward(30)
    leo.right(144)
leo.end_fill()

# Quarta estrela
leo.up()
leo.goto(-150, 60)  # Posição da quarta estrela menor
leo.down()
leo.fillcolor('yellow')
leo.begin_fill()
for i in range(5):
    leo.forward(30)
    leo.right(144)
leo.end_fill()

# Esconde o ícone da tartaruga
leo.hideturtle()

# Fica esperando até que o usuário clique para fechar a tela
turtle.exitonclick()
