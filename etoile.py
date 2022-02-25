def etoile(turtle, longueur, retrait, angle):
    turtle.setheading(0)
    turtle.pendown()

    for nb in range(0, longueur, retrait):
        turtle.forward(longueur - nb)
        turtle.right(180 - angle)

    turtle.penup()
