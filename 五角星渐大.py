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
a = 100
b = 144
n = 0
colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "black", "gray"]
speed(0)
"""1最慢，到10渐大，0最大"""
for i in range(102):
    color(colors[i % 10], colors[i % 10])
    # begin_fill()
    """填充，想要的话就把这俩注释取消"""
    for ii in range(5):
        fd(a)
        right(b)
        """五角星"""
    # end_fill()
    seth(0)
    pu()
    bk(5)
    seth(90)
    fd(1.62459848)
    pd()
    seth(0)
    a += 10
    right(10 * n)
    """改变画笔位置和方向(殆)，五角星边长，内置for画更大五角星"""
hideturtle()
"""隐藏画笔"""
# getcanvas().postscript(file="五角星渐大效果图.eps")
# img = Image.open("五角星渐大效果图.eps")
"""生成效果图，但打开eps得绕点弯儿，需要的话就取消注释吧"""
done()
