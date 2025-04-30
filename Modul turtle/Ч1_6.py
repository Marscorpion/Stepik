import turtle

def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)

def cells(size, num):
    for _ in range(num):
        hexagon(size)
        turtle.right(60)
        turtle.forward(num)
        turtle.right(60)
        turtle.forward(num)
        hexagon(50)

cells(100,5)