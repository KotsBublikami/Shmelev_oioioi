import turtle
import random
screen = turtle.Screen
screen.setup(width = 1.0, height = 1.0)
PCard_1 = turtle.Turtle
PCard_1.color = ("red")
PCard_1.shape = ("sqare")
PCard_1.shapesize(stretch_wid = 5, stretch_len = 10)
PCard_2 = turtle.Turtle
PCard_2.color = ("red")
PCard_2.shape = ("square")
PCard_2.shapesize(stretch_wid = 5, stretch_len = 10)
Comp_Card_1 = turtle.Turtle
Comp_Card_1.color = ("red")
Comp_Card_1.shape = ("sqare")
Comp_Card_2.shapesize(stretch_wid = 5, stretch_len = 10)
Comp_Card_2 = turtle.Turtle
Comp_Card_2.color = ("red")
Comp_Card_2.shape = ("square")
Comp_Crad_2.shapesize(stretch_wid = 5, stretch_len = 10)
def raspr (card,  m, r):
    card = turtle.Turtle()
    card.color = ("green")
    card.shapesize(5, 10)
    if m == 1:
        card.goto(-200, -200)    
    if m == 2:
        card.goto(200, 200)
    if m == 3:
        card.goto(150, 200)
    if m == 4:
        card.goto(-150, 200)

