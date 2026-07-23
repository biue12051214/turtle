from turtle import *
from PIL import Image


speed(0)
"""画图速度，0最快，1最慢，10较快"""
shape("turtle")


def dan(x, y, r):
    pu()
    seth(0)
    goto(x, y-r)
    pd()
    circle(r)


def dans(x, y, ra):
    dan(x, y, ra)
    if ra >= 6:
        dans(x+1.5*ra, y, ra/2)
        dans(x-1.5*ra, y, ra/2)
        dans(x, y+1.5*ra, ra/2)
        dans(x, y-1.5*ra, ra/2)


hideturtle()
tracer(False)
dans(0, 0, 100)
# getcanvas().postscript(file="递归圆效果图.eps")
# img = Image.open("递归圆效果图.eps")
"""生成效果图，但打开eps得绕点弯儿，需要的话就取消注释吧"""
done()
