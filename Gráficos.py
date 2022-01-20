#gráficos.py

import turtle
pen = turtle.Pen()
turtle.bgcolor("black")
pen.width(2)
#         0       1         2       3        4           5
cores = ["red", "yellow", "blue", "green", "orange", "purple"]
pen.speed(0)

for x in range(300):
    cor = cores[x%6] #0,1,2,3
    pen.pencolor(cor)
    pen.circle(x*5)
    pen.left(60)
    
