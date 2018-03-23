#!/usr/bin/python3
import turtle as t



t.shape("turtle")
t.color("yellow", "green")
t.begin_fill()
t.right(15)
t.circle(250,steps=3)
t.end_fill()
t.color("yellow", "green")
t.begin_fill()
for _ in range(3):
    t.left(45)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
t.end_fill()
t.color("yellow", "blue")
t.begin_fill()
t.circle(50)
t.end_fill()
t.begin_fill()
t.color("red", "yellow")
for _ in range(30):
    t.forward(200)
    t.left(170)
t.end_fill()
t.write("we are Chinese",font=('Arial', 40, 'normal'))
t.exitonclick()
#t.done()