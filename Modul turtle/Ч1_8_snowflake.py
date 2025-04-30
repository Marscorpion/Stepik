import turtle

def rhomb(side):
    for _ in range(10):
        turtle.left(35)
        for _ in range(2):
            turtle.forward(side)
            turtle.right(60)
            turtle.forward(side)
            turtle.right(120)


rhomb(100)