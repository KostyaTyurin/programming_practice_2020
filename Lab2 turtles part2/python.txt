import turtle as tr
import numpy as np
tr.shape('turtle')
tr.color('red')
tr.pencolor('black')

tr.left(45)
tr.fd(10 * np.sqrt(2))
tr.right(135)
tr.fd(20)
tr.right(180)
tr.fd(20)


tr.penup()
tr.goto(15, 10)
tr.pendown()

tr.right(180)
tr.fd(10)
tr.left(90)
tr.fd(10)
tr.left(90)
tr.fd(10)
tr.left(180)
tr.fd(20)

tr.penup()
tr.goto(30, 10)
tr.fd(10)
tr.pendown()

tr.left(135)
tr.fd(10 * np.sqrt(2))
tr.right(135)
tr.fd(20)
tr.right(180)
tr.fd(20)

tr.penup()

tr.goto(45, 10)
tr.pendown()

tr.right(90)
tr.fd(10)
tr.right(135)
tr.fd(10*np.sqrt(2))
tr.left(45)
tr.fd(10)
tr.left(180)
tr.fd(10)
tr.right(45)
tr.fd(10 * np.sqrt(2))
tr.left(135)
tr.fd(10)


tr.penup()
tr.goto(60, 10)
tr.pendown()

tr.left(90)
tr.fd(20)
tr.left(90)
tr.fd(10)
tr.left(90)
tr.fd(20)
tr.left(90)
tr.fd(10)

tr.penup()
tr.goto(75, 10)
tr.pendown()

tr.left(90)
tr.fd(20)
tr.left(90)
tr.fd(10)
tr.left(90)
tr.fd(20)
tr.left(90)
tr.fd(10)

tr.exitonclick()