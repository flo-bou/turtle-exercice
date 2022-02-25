from turtle import *
from letter import *
from rectangle import *
from triangle import *
from losange import *
from cercle import *
from spirale import *
from etoile import *
from sapin import *

screen = Screen()
screen.title("Exercice de la tortue")

# turtle to create letters
turtle_letter = RawTurtle(screen)
turtle_letter.penup()
turtle_letter.speed(0)
# I L T
turtle_letter.goto(-450, 350)
path_I(turtle_letter)
turtle_letter.goto(-325, 350)
path_L(turtle_letter)
turtle_letter.goto(-200, 350)
path_T(turtle_letter)
# TILT
turtle_letter.goto(50, 350)
path_T(turtle_letter)
turtle_letter.goto(100, 350)
path_I(turtle_letter)
turtle_letter.goto(150, 350)
path_L(turtle_letter)
turtle_letter.goto(200, 350)
path_T(turtle_letter)
turtle_letter.goto(0, 0)


# turtle to create rectangles
turtle_rectangle = RawTurtle(screen)
turtle_rectangle.penup()
turtle_rectangle.speed(0)
# rectangle vide
turtle_rectangle.goto(-450, 200)
rectangle_vide(turtle_rectangle, 150, 50)
# rectangle plein
turtle_rectangle.goto(-200, 200)
rectangle_plein(turtle_rectangle, 150, 50)
# carré vide
turtle_rectangle.goto(0, 200)
rectangle_vide(turtle_rectangle, 50, 50)
# carré plein
turtle_rectangle.goto(100, 200)
rectangle_plein(turtle_rectangle, 50, 50)
turtle_rectangle.goto(0, 0)


# turtle to create triangles
turtle_triangle = RawTurtle(screen)
turtle_triangle.penup()
turtle_triangle.speed(0)
# triangle isocèle rectangle vers haut gauche
turtle_triangle.goto(-450, 100)
triangle_isocele_rectangle_haut_gauche(turtle_triangle, 25)
# triangle isocèle rectangle vers haut droite
turtle_triangle.goto(-300, 100)
triangle_isocele_rectangle_haut_droite(turtle_triangle, 25)
# triangle isocèle rectangle vers bas gauche
turtle_triangle.goto(-250, 100)
triangle_isocele_rectangle_bas_gauche(turtle_triangle, 25)
# triangle isocèle rectangle vers bas droite
turtle_triangle.goto(-100, 100)
triangle_isocele_rectangle_bas_droite(turtle_triangle, 25)
# triangle isocèle rectangle vers le bas
turtle_triangle.goto(0, 100)
triangle_isocele_rectangle_bas(turtle_triangle, 20)
# triangle isocèle rectangle vers le haut
turtle_triangle.goto(100, 100)
triangle_isocele_rectangle_haut(turtle_triangle, 20)

# losange droit (carré)
turtle_triangle.goto(200, 20)
losange(turtle_triangle, 20)
turtle_triangle.goto(0, 0)


# turtle to create circles
turtle_circle = RawTurtle(screen)
turtle_circle.penup()
turtle_circle.speed(0)
# cercles
turtle_circle.goto(300, 25)
circle_with_dot(turtle_circle, 300)
turtle_circle.goto(300, 100)
circle_as_polygon(turtle_circle, 500)
turtle_circle.goto(0, 0)


# turtle to create spirals
turtle_spirale = RawTurtle(screen)
turtle_spirale.penup()
turtle_spirale.speed(0)
# spirales
turtle_spirale.goto(-400, -100)
spirale_carre(turtle_spirale, 200, 5)
turtle_spirale.goto(-150, -70)
spirale_carre(turtle_spirale, 300, 10)
turtle_spirale.goto(0, 0)


# turtle to create stars
turtle_etoile = RawTurtle(screen)
turtle_etoile.penup()
turtle_etoile.speed(0)
# stars
turtle_etoile.goto(100, -100)
etoile(turtle_etoile, 200, 2, 22)
turtle_etoile.goto(200, -200)
etoile(turtle_etoile, 300, 5, 12)
turtle_etoile.goto(0, 0)


# turtle to create pine trees
turtle_sapin = RawTurtle(screen)
turtle_sapin.penup()
turtle_sapin.speed(0)
# pine trees
turtle_sapin.goto(-300, 0)
sapin(turtle_sapin, 3)
turtle_sapin.goto(-100, 0)
sapin(turtle_sapin, 6)
turtle_sapin.goto(0, 0)


screen.exitonclick()
