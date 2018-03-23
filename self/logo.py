#!/usr/bin/python3
import turtle as t

t.shape("turtle")
t.color("green", "LightSkyBlue")
t.begin_fill()
t.right(15)
t.circle(200,steps=3)
t.end_fill()

print (t.heading())
t.color("green", "DodgerBlue")
t.begin_fill()
t.right(60)
t.circle(160,steps=3)
t.end_fill()

t.color("green", "Blue")
t.begin_fill()
t.right(60)
t.circle(128,steps=3)
t.end_fill()

t.color("green", "NavyBlue")
t.begin_fill()
t.right(60)
t.circle(104,steps=3)
t.end_fill()

t.penup()
t.left(75)
t.forward(340)
t.pendown()
t.pencolor("black")
t.write("Synchronoss Inc.",font=('Arial', 50, 'normal'))
t.hideturtle()
t.exitonclick()