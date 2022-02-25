from triangle import *
from rectangle import *

def sapin(turtle, dimension):
    (pos_x, pos_y) = turtle.position() # position will be the highest point of the pine tree
    turtle.penup()
    turtle.pencolor("green")

    for i in range(1, dimension + 1):
        turtle.goto(pos_x, pos_y)
        triangle_isocele_rectangle_haut(turtle, i * 10)
        pos_y = pos_y - i * 5

    turtle.penup()
    pos_y = turtle.ycor()
    turtle.goto(pos_x - int(dimension * 2.5), pos_y)
    turtle.pencolor("brown")
    rectangle_plein(turtle, dimension * 5, dimension * 7)

    turtle.penup()
    turtle.pencolor("black")
