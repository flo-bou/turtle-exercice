
def spirale_carre(turtle, longueur, retrait):
    turtle.setheading(0)
    turtle.pendown()

    for nb in range(0, int(longueur), retrait):
        turtle.forward(longueur - nb)
        turtle.right(90)
        turtle.forward(longueur - nb)
        turtle.right(90)

    turtle.penup()
