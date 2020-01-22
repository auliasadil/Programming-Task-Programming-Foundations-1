import turtle
from random import randint

turtle.setup(1000, 700)
turtle.title('Rotating Squares and Disks with Random Colors')
value = int(turtle.numinput('Rotating Colorful Squares and Disks',\
                'Please enter the side length of the first square[20-60]:' \
                , 40, minval = 20, maxval = 60))

#for the squares
turtle.ht()
turtle.up()
turtle.speed(0)
turtle.goto(-250, 100)
side_length = value
angle_of_change = 5
turtle.down()
turtle.left(160)
for i in range(72):
    turtle.colormode(255)
    turtle.fillcolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    turtle.begin_fill()
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.end_fill()
    turtle.right(angle_of_change)
    side_length += 2

#for the circles
radius = side_length/2
turtle.up()
turtle.goto(250, 0)
turtle.down()
angle = 0
for i in range(36):
    turtle.seth(angle)
    turtle.colormode(255)
    turtle.fillcolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    angle += 10
    radius -= 2

#for the writing
turtle.up()
turtle.goto(0, -300)
turtle.down()
turtle.color('blue')
turtle.write('There are 72 Squares and 36 Disks', move = False, align = 'center', font = ('', 20, 'normal'))
turtle.ht()
turtle.exitonclick()
    

