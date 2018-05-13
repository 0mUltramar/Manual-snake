" Нарисуй хризантему из квадратов, нарисованных черепашкой "
import turtle


def drawing_square():
    i = 0
    for i in range(4):
        turtle.forward(50)
        i += 1
        if i < 4:
            turtle.left(90)
    pass

def make_sqaures():
    i = 0
    for i in range (19):
        drawing_square()
        turtle.left(20)
    turtle.exitonclick()

make_sqaures()