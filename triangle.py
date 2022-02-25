from ligne import *

def triangle_isocele_rectangle_haut_gauche(turtle, largeur): # drawing starts at the top left
    turtle.pendown()
    for i in range(int(largeur)):
        ligne_vers_droite_et_retour(turtle, largeur - i)
    turtle.penup()

def triangle_isocele_rectangle_haut_droite(turtle, largeur): # drawing starts at the top right
    turtle.pendown()
    for i in range(int(largeur)):
        ligne_vers_gauche_et_retour(turtle, largeur - i)
    turtle.penup()

def triangle_isocele_rectangle_bas_gauche(turtle, largeur): # drawing starts at the top left
    turtle.pendown()
    for i in range(int(largeur)):
        ligne_vers_droite_et_retour(turtle, i + 1)
    turtle.penup()

def triangle_isocele_rectangle_bas_droite(turtle, largeur): # drawing starts at the top right
    turtle.pendown()
    for i in range(int(largeur)):
        ligne_vers_gauche_et_retour(turtle, i + 1)
    turtle.penup()


def triangle_isocele_rectangle_haut(turtle, hauteur): # drawing starts at the top center
    (pos_x, pos_y) = turtle.position()
    triangle_isocele_rectangle_bas_droite(turtle, hauteur)
    turtle.goto(pos_x, pos_y)
    triangle_isocele_rectangle_bas_gauche(turtle, hauteur)

def triangle_isocele_rectangle_bas(turtle, hauteur): # drawing starts at the top center
    (pos_x, pos_y) = turtle.position()
    triangle_isocele_rectangle_haut_droite(turtle, hauteur)
    turtle.goto(pos_x, pos_y)
    triangle_isocele_rectangle_haut_gauche(turtle, hauteur)
