from turtle import *
# from PIL import Image


speed(0)
"""画图速度，0最快，1最慢，10较快"""
shape("turtle")
bgcolor("blueviolet")
"""画布颜色"""
n = 1
ang_w = 2
ang_r = 7
ang_b = 2
ang_bl = 7
"""依次是白红黑蓝的角度"""
r = 100
r_zheng = 100
"""最外层圆的直径,两个r值要一起改改一样"""
r_ = 25
"""单个圆每次r减小"""
yuan = 4
"""单个圆有几个圆"""
yuan_pan = 9
"""单个圆圆偏转角度，两个ang_相加∠可以营造错位效果"""
num = int(360 / (ang_r + ang_b + ang_w + ang_bl))
dis_x = 250
dis_y = 240
"""单个圆与单个圆x,y的相离距离"""


def single(x, y):
    global ang_b
    global ang_r
    global ang_w
    global ang_bl
    global r
    global yuan_pan
    global n
    pu()
    goto(x, y)
    fd(r)
    left(90)
    if n == 1:
        circle(r, yuan_pan)
    else:
        pass
    pd()
    fillcolor("white")
    """白色扇形填充"""
    begin_fill()
    circle(r, ang_w)
    left(90)
    fd(r)
    end_fill()
    fillcolor("red")
    """红色扇形填充"""
    begin_fill()
    bk(r)
    right(90)
    circle(r, ang_r)
    left(90)
    fd(r)
    end_fill()
    fillcolor("black")
    """黑色扇形填充"""
    begin_fill()
    bk(r)
    right(90)
    circle(r, ang_b)
    left(90)
    fd(r)
    end_fill()
    fillcolor(0, 0.7, 0.7)
    """偏蓝色扇形填充"""
    begin_fill()
    bk(r)
    right(90)
    circle(r, ang_bl)
    left(90)
    fd(r)
    end_fill()
    left(180)
    n += 1


for ii in range(-1, 2):
    """-1列到2-1=1列"""
    x = ii * dis_x
    for iii in range(-1, 2):
        """-1行到2-1=1行"""
        y = iii * dis_y
        for iv in range(yuan):
            for i in range(num):
                single(x, y)
            r -= r_
            n = 1
            if r == r_zheng - r_ * yuan:
                r = r_zheng

hideturtle()
getcanvas().postscript(file="旋转蛇效果图.eps")
# img = Image.open("旋转蛇效果图.eps")
# """生成效果图，但打开eps得绕点弯儿，需要的话就取消注释吧"""
done()
