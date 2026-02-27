import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Setup turtle
tree = turtle.Turtle()
tree.speed(0)
tree.left(90)
tree.penup()
tree.goto(0, -250)
tree.pendown()
tree.color("brown")
tree.hideturtle()

def draw_branch(length):
    if length < 10:
        tree.color("green")
        tree.stamp()  # Cetak daun
        tree.color("brown")
        return
    
    tree.pensize(length / 10)
    tree.forward(length)
    
    angle = random.randint(15, 35)
    
    tree.right(angle)
    draw_branch(length - random.randint(10, 20))
    
    tree.left(angle * 2)
    draw_branch(length - random.randint(10, 20))
    
    tree.right(angle)
    tree.backward(length)

# Gambar pohon
draw_branch(100)

# Selesai
turtle.done()