import turtle
import random
import time

wn = turtle.Screen()
wn.title("Шмелев")
wn.bgcolor("black")
Weight_screen = 800
Height_screen = 800
wn.setup(width=Weight_screen, height=Height_screen)
wn.tracer(0)

shmel = turtle.Turtle()
shmel.speed(0)
shmel.shape("circle")
shmel.color("white")
shmel.shapesize(stretch_wid=3)
shmel.penup()
shmel.goto(0, 0)

def shmel_up():
    y = shmel.ycor()
    y += 20
    shmel.sety(y)

def shmel_down():
    y = shmel.ycor()
    y -= 20
    shmel.sety(y)

def shmel_left():
    x = shmel.xcor()
    x -= 20
    shmel.setx(x)

def shmel_right():
    x = shmel.xcor()
    x += 20
    shmel.setx(x)


wn.listen()
wn.onkeypress(shmel_up, "Up")
wn.onkeypress(shmel_down, "Down")
wn.onkeypress(shmel_left, "Left")
wn.onkeypress(shmel_right, "Right")

arr_rebenok = [] # заполните
koef = [-1, 1]
rebenok = turtle.Turtle()
rebenok.speed(0)
rebenok.shape("square")
rebenok.color("white")
rebenok.shapesize(stretch_wid=0.5, stretch_len=0.5)
rebenok.penup()
random.shuffle(koef)
rebenok.dx = random.randint(10, 20) / 100 * koef[0]
random.shuffle(koef)
rebenok.dy = random.randint(10, 20) / 100 * koef[0]
rebenok.goto(random.randint(-800, 800), random.randint(-800, 800))
arr_rebenok.append(rebenok) # добавить всех

def dist(reb):
    return ((shmel.xcor() - reb.xcor()) ** 2 + (shmel.ycor() - reb.ycor()) ** 2) ** 0.5

def checker_stolknovenia(reb):
    if dist(reb) <= 10:
        return True
    else:
        return False


def check_granica(fig):
    if fig.ycor() > 800:
        fig.sety(-800)
    if fig.ycor() < -800:
        fig.sety(800)
    if fig.xcor() < -800:
        fig.setx(800)
    if fig.xcor() > 800:
        fig.setx(-800)

count_hod = 0
game_over = False
while not game_over:
    wn.update()
    # Движение детей вот здесь двигаешь
    rebenok.setx(rebenok.xcor() + rebenok.dx)
    rebenok.sety(rebenok.ycor() + rebenok.dy)
    count_hod += 1
    if count_hod == 7500:
        random.shuffle(koef)
        rebenok.dx = random.randint(10, 20) / 100 * koef[0]
        random.shuffle(koef)
        rebenok.dy = random.randint(10, 20) / 100 * koef[0]
        count_hod = 0
        print(rebenok.dx, rebenok.dy)
    # Отскок от верхней и нижней границы
    if rebenok.ycor() > 800 or rebenok.ycor() < -800 or rebenok.xcor() < -800 or rebenok.xcor() > 800:
        check_granica(rebenok)

    # Проверка на поимку
    if checker_stolknovenia(rebenok):
        rebenok.color("black")
        ind = arr_rebenok.index(rebenok)
        arr_rebenok = arr_rebenok[0:ind] + arr_rebenok[ind + 1:]
        # удаляешь из списка детей

    # Проверка на победу
    if len(arr_rebenok) == 0:
        game_over = True
        time.sleep(3)

wn.bye()
