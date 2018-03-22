#!/usr/bin/python3

import turtle as t

print (t.position())
t.color("blue")

num = 0
while num < 5:
    # 当前位置拷贝一份箭头形状
    stamp_id = t.stamp()
    t.fd(50)
    num += 1
t.pensize(15)
t.forward(200)
t.right(90)
t.dot(50, "blue")
t.forward(200)
t.right(90)
t.dot(50, "red")
t.forward(200)
t.right(90)
t.dot(50, "yellow")
t.forward(200)
t.dot(50, "pink")
print (t.position())

t.done()