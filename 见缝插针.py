from turtle import *
from time import *
import math
from datetime import datetime


def redy():
    pu()
    goto(0, -50)
    setheading(0)
    pd()
    pencolor("violet")
    fillcolor("violet")
    begin_fill()
    circle(50)
    end_fill()


class Needle:
    def __init__(self, a):
        self.angle = a

    def draw(self):
        color("black")
        pensize(2)
        pu()
        goto(0, 0)
        seth(self.angle)
        fd(50)
        pd()
        pencolor("blue")
        fd(50)
        color("black")
        write("O", align="left", font=("宋体", 7))
        if not game:
            pu()
            goto(-250, -70)
            pd()
            color("green")
            write("GameOver", align="left", font=("italic", 20))
            pu()
            goto(200, -90)
            pd()
            color(0.3, 0.6, 0.7)
            a = "\n".join("摁r重新开始")
            write(a, align="left", font=("italic", 20))

    def update(self):
        self.angle += 1
        self.angle = self.angle % 360


def add(x, y):
    global game
    global n
    a = 0
    if not game:
        return
    try:
        a = math.degrees(math.atan(y / x))
    except ZeroDivisionError:
        if y > 0:
            a = 90
        elif y < 0:
            a = 270
    if y == 0:
        if x >= 0:
            a = 0
        elif x < 0:
            a = 180
    if x > 0 and y > 0:
        pass
    elif x > 0 > y:
        a += 360
    else:
        a += 180
    new = Needle(a)
    for i in needles:
        if abs(i.angle - new.angle) <= 4:
            game = False
            new.draw()
    needles.append(new)
    n += 1


def on_key_q():
    global game
    game = False
    bye()


def on_key_space():
    global game
    if not game:
        game = True
        run()
    else:
        game = False
        pu()
        goto(200, -90)
        pd()
        color(0.3, 0.6, 0.7)
        a = "\n".join("摁r重新开始")
        write(a, align="left", font=("bolt italic", 25))


def on_key_r():
    global game
    global needles
    global n
    if not game:
        n = 0
        needles = []
        game = True
        run()
    else:
        pass


n = 0
hideturtle()
speed(0)
shape("turtle")
game = True
setup(600, 400)
needle = Needle
needles = []
onscreenclick(add)
onkeypress(on_key_q, "q")
onkeypress(on_key_space, "space")
onkeypress(on_key_r, "r")
listen()


def run():
    while game:
        tracer(False)
        clear()
        pu()
        goto(0, 150)
        color("black")
        td = datetime.today()
        tds = str(td.second)
        tdm = str(td.minute)
        tdh = str(td.hour)
        write(tdh + ": " + tdm + ": " + tds, align="center", font=("宋体", 20))
        pu()
        goto(-250, 50)
        color("red")
        pd()
        write("得分: " + str(n), align="left", font=("宋体", 20))
        pu()
        goto(-250, -160)
        color("blueviolet")
        pd()
        write("英文键盘摁'q'结束游戏", align="left", font=("宋体", 20))
        pu()
        goto(-250, -183)
        color("blueviolet")
        pd()
        write("空格暂停游戏，当游戏结束时空格将继续", align="left", font=("宋体", 15))
        for needle in needles:
            needle.update()
            needle.draw()
        redy()
        tracer(True)
        sleep(0.01)


run()
done()
