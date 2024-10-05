import turtle

turtle.title("My First Turtle")
screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(400,400)

t = turtle.Turtle()
t.color("red")
#forward, backward, left, right
#square
t.backward(100)
t.right(90)
t.backward(100)
t.right(90)
t.backward(100)
t.right(90)
t.backward(100)
#triangle
for _ in range(3):
    t.forward(100)
    t.left(120)
#hexagon
for _ in range(6):
    t.forward(100)
    t.left(60)
#rectangle
t.forward(70)
t.right(90)
t.forward(150)
t.right(90)
t.forward(70)
t.right(90)
t.forward(150)
turtle.done()