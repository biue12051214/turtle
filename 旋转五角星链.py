from turtle import *
from time import *
# from PIL import Image


Alice = "D:\\python\\pythonProject2\\小海龟Turtle\\Alice.gif"
register_shape(Alice)
shape(Alice)
pu()
fd(200)
right(30)
fd(150)
sleep(0.5)
home()
pd()
sleep(0.5)
shape("turtle")
colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "black", "gray"]
speed(0)
for iii in range(9):
    """九条链"""
    pu()
    home()
    pd()
    right(40 * iii)
    a = 30
    b = 144
    n = 0
    for i in range(19):
        """链上19颗星"""
        color(colors[i % 10], colors[i % 10])
        begin_fill()
        for ii in range(5):
            """五角星"""
            fd(a)
            right(b)
            a += 0.5
        end_fill()
        fd(25)
        n += 0.1
        right(10 * n)
hideturtle()
# getcanvas().postscript(file="旋转五角星链效果图.eps")
# img = Image.open("旋转五角星链效果图.eps")
"""生成效果图，但打开eps得绕点弯儿，需要的话就取消注释吧"""
done()
