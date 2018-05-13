""" Нарисовать квадрат черепашкой """

import turtle

# делаем черепашку черепашкой)
turtle.shape("turtle")

turtle.color("red")

# попросим черепашку нарисовать квадрат
def drawing_square():
    i = 0
    for i in range(4):
        turtle.forward(50)
        i += 1
        if i < 4:
            turtle.left(90)
    turtle.exitonclick()

# призываем черепашку
drawing_square()

