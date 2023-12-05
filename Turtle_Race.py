import random
from turtle import Turtle, Screen
from tkinter import simpledialog

class TurtleAtt:
    def __init__(self, shape, color, x, y):
        self.colors = color
        self.shapes = shape
        self.turtle_instance = Turtle()
        self.start_width = int(x)
        self.start_height = int(y)

    def setup_turtle(self):
        self.turtle_instance.color(self.colors)
        self.turtle_instance.shape(self.shapes)
        self.turtle_instance.penup()
        self.turtle_instance.goto(self.start_width, self.start_height)

    def move_forward(self):
        self.turtle_instance.forward(random.randint(1,5))



end = False
screen = Screen()

screen.setup(500, 400)
user_bet = screen.textinput("Betting", "Who do you want to bet on:")

tom = TurtleAtt("turtle", "blue", -240, -30)
tom.setup_turtle()


tim = TurtleAtt("turtle", "red", -240, -50)
tim.setup_turtle()


jen = TurtleAtt("turtle","pink",-240, -10)
jen.setup_turtle()


jade = TurtleAtt("turtle","purple",-240, 10)
jade.setup_turtle()


andy = TurtleAtt("turtle","orange",-240, 30)
andy.setup_turtle()

screen.delay(10)

while not end:
    andy.move_forward()
    jade.move_forward()
    jen.move_forward()
    tim.move_forward()
    tom.move_forward()
    if any(turtle.turtle_instance.xcor() >= 240 for turtle in [andy, jade, jen, tim, tom]):
        end = True
        if any(turtle.turtle_instance.xcor() >= 240 for turtle in [andy, jade, jen, tim, tom]):
            end = True
            winner = None
            if andy.turtle_instance.xcor() >= 240:
                winner = "orange"
            elif jade.turtle_instance.xcor() >= 240:
                winner = "purple"
            elif jen.turtle_instance.xcor() >= 240:
                winner = "pink"
            elif tim.turtle_instance.xcor() >= 240:
                winner = "red"
            elif tom.turtle_instance.xcor() >= 240:
                winner = "blue"

            if winner and user_bet.lower() == winner.lower():
                message = f"Congratulations! You win! {winner} crossed the finish line."
            else:
                message = f"Sorry, you lost. The winner is {winner}."

            screen.bye()  # Close the screen to avoid interference with the message box
            simpledialog.messagebox.showinfo("Race Result", message)
