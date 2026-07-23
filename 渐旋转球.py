from turtle import *
# from PIL import Image


speed(0)
shape("turtle")
bgcolor(0.3, 0.6, 0.1)
"""画布颜色0-1"""
fillcolor("gray")
"""填充颜色"""
setup(700, 500, 700, 100)
n = 1
m = 1
h = 7
"""行数"""
l = 12
"""列数"""
hjuli = 50
"""每行球与球的距离"""
ljuli = 70
"""每列球与球的距离"""
geshu = h * l
"""球总个数"""
r = 21
"""球半径"""


def round_line():
    """单个球"""
    global r
    global m
    begin_fill()
    pensize(3)
    pencolor("red")
    circle(r, 180)
    pencolor("blue")
    circle(r, 180)
    end_fill()
    m += 1


def volu_cir():
    """边缘旋转效果"""
    global r
    global geshu
    pu()
    circle(r, 360/geshu * (m-1))
    pd()


def every_line():
    """单一行"""
    global l
    global hjuli
    global ljuli
    global n
    global m
    for ii in range(l):
        pu()
        if m % l == 0:
            goto(-300 + l * hjuli, 270 - n * ljuli)
        else:
            goto(-300 + m % l * hjuli, 270 - n * ljuli)
        seth(0)
        volu_cir()
        pd()
        round_line()


for i in range(h):
    every_line()
    n += 1
hideturtle()
# getcanvas().postscript(file="渐旋转球效果图.eps")
# img = Image.open("渐旋转球效果图.eps")
"""生成效果图，但打开eps得绕点弯儿，需要的话就取消注释吧，PS可以打开"""
done()
