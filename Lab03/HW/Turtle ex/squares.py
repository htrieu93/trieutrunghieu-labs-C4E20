from turtle import *

#Ex 3:
def draw_square(length, square_color):
    speed(4)
    color(square_color)
    for line in range(4):
        forward(length)
        left(90)

    mainloop()

#Ex 4:
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()