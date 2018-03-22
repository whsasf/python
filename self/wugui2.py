#!/usr/bin/python3
import turtle

def drawSnake(rad, angle, len, neckrad):
    for _ in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.forward(rad/2)  # 
    turtle.circle(neckrad, 180)
    turtle.forward(rad/4)

if __name__ == "__main__":
   turtle.setup(1500, 1400, 0, 0)
   turtle.pensize(30)  # 
   turtle.pencolor("green")
   turtle.seth(-40)    # 
   drawSnake(70, 80, 2, 15)

turtle.done()
