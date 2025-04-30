import turtle

def star(size):
    for _ in range(12):
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(30)

star(100)