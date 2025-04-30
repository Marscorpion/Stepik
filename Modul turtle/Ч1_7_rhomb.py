import turtle

def rhomb(side):
    for _ in range(2):
        turtle.forward(side)
        turtle.left(120)
        turtle.forward(side)
        turtle.left(60)


rhomb(100)