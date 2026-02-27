import turtle

t = turtle.Turtle()
t.speed(3)

def pindah(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

pindah(-200, 100)
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)

pindah(-50, 100)
for _ in range(3):
    t.forward(80)
    t.left(120)

pindah(100, 100)
t.forward(100)
t.left(120)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.setheading(0)

pindah(-200, -50)
for _ in range(2):
    t.forward(100)
    t.left(60)
    t.forward(50)
    t.left(120)

pindah(50, -50)
for _ in range(2):
    t.forward(70)
    t.left(60)
    t.forward(70)
    t.left(120)

turtle.done()