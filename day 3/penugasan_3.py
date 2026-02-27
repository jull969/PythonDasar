import turtle

t = turtle.Turtle()

t.fillcolor("red")
t.begin_fill()
for _ in range(2):
    t.forward(200); t.left(90); t.forward(60); t.left(90)
t.end_fill()

t.goto(0, -60)
t.fillcolor("white")
t.begin_fill()
for _ in range(2):
    t.forward(200); t.left(90); t.forward(60); t.left(90)
t.end_fill()

turtle.done()