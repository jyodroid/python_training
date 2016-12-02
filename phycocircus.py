import turtle


def draw_square(my_turtle):

    for steps in xrange(4):
        my_turtle.forward(100)
        my_turtle.right(90)


def draw_circle_with_squarees():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(100)

    for steps in xrange(73):
        draw_square(brad)
        brad.right(5)

    window.exitonclick()

draw_circle_with_squarees()
