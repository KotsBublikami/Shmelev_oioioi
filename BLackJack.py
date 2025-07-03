import turtle
import random
screen = turtle.Screen
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
def zn():
    number = random.randint(2,11)
    if number == 11:
        number = "A"
    kartink = ["10","Q","K","J" ]
    if number == 10:
        number = random.choise(kartink)
    return(number)
    
def twoten(m):
    card = turtle.Turtle()
    card.color = ("green")
    card.shapesize(5, 10)
    if m == 1:
        card.goto(-200, -200)
        card.write("zn")
    if m == 2:
        card.goto(200, 200)
        card.write("zn")
    if m == 3:
        card.goto(150, 200)
        card.write("zn")
    if m == 4:
        card.goto(-150, 200)
        card.write("zn")
 
    
    
