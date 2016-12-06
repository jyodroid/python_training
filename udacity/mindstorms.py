import turtle


def draw_square(my_turtle):

    for steps in xrange(4):
        my_turtle.forward(100)
        my_turtle.right(90)


def draw_circle(my_turtle):
    my_turtle.circle(60)


def draw_triangle(my_turtle):
    for steps in xrange(3):
        my_turtle.right(120)
        my_turtle.forward(100)


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    steve = turtle.Turtle()
    steve.shape("classic")
    steve.color("green")

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")

    draw_circle(brad)
    draw_triangle(angie)
    draw_square(steve)

    window.exitonclick()


draw_shapes()
