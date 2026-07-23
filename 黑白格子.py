from turtle import *
from time import *
from PIL import Image


speed(0)
shape("turtle")
setup(600, 600, 900, 100)
pu()
goto(-200, 200)
pd()
speed(0)
n = 0
h = 0
m = 9
"""m表示每行格数，为奇数"""
for iv in range(9):
    """9表示行数"""
    h += 1
    # n += 1
    """如果m为偶数，上1行取消注释以得到交错格子"""
    for i in range(m):
        n += 1
        if n % 2 == 0:
            """如果以黑格子开头，改成1变白格子，反之亦然，奇偶都一样"""
            fillcolor("white")
            begin_fill()
            for ii in range(4):
                fd(50)
                right(90)
            end_fill()
        else:
            fillcolor("black")
            begin_fill()
            for iii in range(4):
                fd(50)
                right(90)
            end_fill()
        fd(50)
    right(90)
    fd(50)
    left(90)
    bk(m * 50)
hideturtle()
sleep(1)
getcanvas().postscript(file="黑白格子效果图.eps")
img = Image.open("黑白格子效果图.eps")
"""生成效果图，但打开eps得绕点弯儿，需要的话就取消注释吧"""
done()
