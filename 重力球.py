from turtle import *
from time import *
from random import *


speed(0)
"""画图速度，0最快，1最慢，10较快"""
shape("turtle")
n = True
a = 0
b = 0
y = 200
x = 50
"""初始位置，鼠标点击可随时改变小球位置"""
yv = 3
"""初始下降速度"""
xv = 5
"""左右移动速度"""
w = 800
h = 600
setup(w, h, 700)
"""画布长宽"""
hideturtle()
"""隐藏画笔"""
r = randint(30, 70)
"""小球大小，随机30-70"""
co1 = random()
co2 = random()
co3 = random()
"""小球颜色，co123都是[0-1)"""


def yuan():
    global yv
    global xv
    global x
    global y
    if abs(y) >= abs(h/2-r/2):
        yv = -yv
    if abs(x) >= abs(w/2-r/2):
        xv = -xv
    pu()
    goto(x, y)
    pd()

    dot(r, (co1, co2, co3))
    y -= yv
    x += xv
    if yv > 0:
        yv += 0.1
        """速度向下递增0.1"""
    elif yv <= 0:
        yv += 0.11
        """向上递减0.11"""


def on_key_q():
    global n
    n = False


def fun(x_n, y_n):
    global x
    global y
    x = x_n
    y = y_n


def run():
    while n:
        tracer(False)
        clear()
        yuan()
        sleep(0.01)
        tracer(True)


onscreenclick(fun)
onkeypress(on_key_q, "q")
"""英文状态下摁‘q’退出"""
listen()
run()
