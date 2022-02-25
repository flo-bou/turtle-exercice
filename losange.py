from triangle import *

def losange(turtle, demie_diagonale):
    (pos_x, pos_y) = turtle.position()

    triangle_isocele_rectangle_haut(turtle, demie_diagonale)
    turtle.goto(pos_x, pos_y - demie_diagonale)
    triangle_isocele_rectangle_bas(turtle, demie_diagonale)
