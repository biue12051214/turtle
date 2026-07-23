from turtle import *
from random import *
from PIL import Image


"""有点卡是正常状况，稍等片刻or39行注释掉看它慢慢爬"""
speed(0)
"""画图速度，0最快，1最慢，10较快"""
shape("turtle")
bgcolor("black")
setup(1200, 800, 300, 10)


def dans(ra):
    if ra >= 10:
        pensize(ra / 20)
        pencolor("white")
        fd(ra)
        n = randint(10, 20)
        right(n)
        dans(ra-randint(20, 35))
        n_1 = randint(10, 20)
        right(n_1)
        dans(ra - randint(20, 35))
        m_2 = randint(-10, 10)
        left(n + n_1 + m_2)
        dans(ra - randint(20, 35))
        m_1 = randint(10, 20)
        left(m_1)
        dans(ra-randint(10, 20))
        m = randint(10, 20)
        left(m)
        dans(ra-randint(20, 35))
        right(m + m_1 + m_2)
        bk(ra)
    else:
        color('red')
        dot(10)
        color('white')


hideturtle()
tracer(False)
pu()
goto(0, -500)
left(90)
pd()
dans(150)
getcanvas().postscript(file="树效果图.eps")
img = Image.open("树效果图.eps")
"""生成效果图，但打开eps得绕点弯儿，需要的话就取消注释吧"""
done()
