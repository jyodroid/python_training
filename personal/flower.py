import turtle


def draw_diamont(my_turtle):

    for step in range(2):
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.right(135)
        my_turtle.forward(100)

    for step in range(2):
        my_turtle.right(45)
        my_turtle.forward(100)
        my_turtle.left(135)
        my_turtle.forward(100)


def draw_flower():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(100)

    for steps in xrange(75):
        draw_diamont(brad)
        brad.right(5)

    brad.color("white")

    brad.write(
        "Te amo Jeimmy", True, align="center", font=("Arial", 28, "normal"))

    window.exitonclick()

draw_flower()
