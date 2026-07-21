from turtle import *
from time import *
# from PIL import Image


Alice = "D:\\python\\pythonProject2\\小海龟Turtle\\Alice.gif"
register_shape(Alice)
shape(Alice)
"""将画笔替换为图片Alice"""
pu()
fd(200)
right(30)
fd(150)
sleep(0.5)
home()
pd()
sleep(1)
"""开头的图片移动效果"""
shape("turtle")
a = 100
speed(0)
for i in range(1100):
    """循环1100次"""
    fd(a)
    a += 10
    right(190)
    """179也很nice"""
hideturtle()
# getcanvas().postscript(file="螺旋线条效果图.eps")
# img = Image.open("螺旋线条效果图.eps")
"""生成效果图，但打开eps得绕点弯儿，需要的话就取消注释吧"""
done()
