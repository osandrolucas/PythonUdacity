import turtle

window = turtle.Screen()
window.bgcolor("red")


def draw_square():
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(2)
    a = 0
    while (a < 4):
        brad.forward(100)
        brad.right(90)
        a = a + 1


def draw_circle():
    brad1 = turtle.Turtle()
    brad1.color("yellow")
    brad1.shape("turtle")
    brad1.circle(100)


def draw_tri():
    tom = turtle.Turtle()
    tom.forward(100)
    tom.left(120)
    tom.forward(100)
    tom.left(120)
    tom.forward(100)

draw_square()
draw_circle()
draw_tri()
window.exitonclick()



