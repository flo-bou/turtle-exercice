from math import pi

# création du cercle en marquant de multiples points à l'aide du rayon et d'un angle défini à la main
def circle_with_dot(turtle, perimeter):
    (pos_x, pos_y) = turtle.position()
    rayon = int(perimeter / (2 * pi))

    turtle.penup()
    turtle.radians()
    turtle.setheading(0) # vers la droite

    for degree in range(150): # 150 dots
        turtle.forward(rayon)
        turtle.dot(2, "black")
        turtle.goto(pos_x, pos_y)
        turtle.right( 2 * pi / 150)
    
    turtle.penup()
    turtle.degrees()


# représentation du cercle en tant que polygone régulier
def circle_as_polygon(turtle, perimeter):
    nb_cote = 20 # change value for different polygons : 4 = square, 6 = hexagon ...
    angle_interne = (nb_cote - 2) * pi / nb_cote
    largeur_cote = perimeter / nb_cote

    turtle.penup()
    turtle.radians()
    turtle.setheading(180) # le cercle se dessine vers la droite
    turtle.pendown()

    for nb in range(nb_cote):
        turtle.right(pi - angle_interne)
        turtle.forward(largeur_cote)

    turtle.penup()
    turtle.degrees()
