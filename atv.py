import turtle

# Configuração do turtle
leo = turtle.Turtle()
leo.shape("turtle")
leo.pensize(3)
leo.speed(3)

# Função para desenhar uma estrela preenchida corretamente
def draw_star(x, y, size, color="yellow"):
    leo.up()
    leo.goto(x, y - size / 2)  # Ajuste para centralizar a estrela corretamente
    leo.down()
    leo.fillcolor(color)
    leo.begin_fill()
    
    leo.setheading(0)  # Garante que a estrela começa na posição correta
    for _ in range(5):
        leo.forward(size)
        leo.right(144)
    
    leo.end_fill()

# Desenha uma estrela grande no centro
draw_star(0, 0, 100)

# Esconde o cursor e finaliza
leo.hideturtle()
turtle.done()