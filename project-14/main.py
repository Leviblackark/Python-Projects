from turtle import Turtle, Screen
from shapes import Shape

# def move_up():
#     blob.setheading(90)
#     blob.forward(20)

blob = Turtle()

shape = Shape(blob, space_between=50)
blob.pensize(4)
shape.maker()

for _ in range(3):
    shape.walker()
    shape.firework()
    shape.maker()
    shape.nested_shapes()
    shape.firework()


screen = Screen()
# screen.listen()

# screen.onkey(move_up, "w")
screen.exitonclick()
