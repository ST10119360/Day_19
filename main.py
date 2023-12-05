from turtle import Turtle, Screen
"""
Etch a skecth with turtle graphics
"""
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def turn_left():
    tim.left(5)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def turn_right():
    tim.right(5)


def move_backwards():
    tim.backward(10)


screen.listen()
screen.onkeypress(move_backwards, "s")
screen.onkeypress(key="space", fun=move_forward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()
