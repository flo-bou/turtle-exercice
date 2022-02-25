from ligne import *

def rectangle_vide(turtle, largeur, hauteur):
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(largeur)
    turtle.right(90)
    turtle.forward(hauteur)
    turtle.right(90)
    turtle.forward(largeur)
    turtle.right(90)
    turtle.forward(hauteur)
    turtle.penup()

def rectangle_plein(turtle, largeur, hauteur):
    turtle.pendown()
    for ligne in range(hauteur):
        ligne_vers_droite_et_retour(turtle, largeur)
    turtle.penup()
