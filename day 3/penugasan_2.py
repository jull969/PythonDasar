import turtle

t = turtle.Turtle()

def gambar_warna(warna, fungsi_gambar):
    t.fillcolor(warna)
    t.begin_fill()
    fungsi_gambar()
    t.end_fill()

t.penup(); t.goto(-200, 0); t.pendown()
t.fillcolor("red")
t.begin_fill()
for _ in range(2):
    t.forward(100); t.left(90); t.forward(50); t.left(90)
t.end_fill()

turtle.done()