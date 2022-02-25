def ligne_vers_droite_et_retour(turtle, longueur):
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(longueur)
    turtle.penup()
    turtle.backward(longueur)
    turtle.right(90)
    turtle.forward(1)
    turtle.left(90)

def ligne_vers_gauche_et_retour(turtle, longueur):
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(longueur)
    turtle.penup()
    turtle.backward(longueur)
    turtle.left(90)
    turtle.forward(1)
    turtle.right(90)
