import turtle_def_mnogoangles_9 as tr
tr.shape('turtle')
tr.speed(3)
tr.width(5)
tr.turtlesize(2)
tr.color('deepskyblue')
tr.goto(0,0)
for i in range(100, 1100, 100):
    tr.fd(i)
    tr.left(90)
    tr.fd(i)
    tr.left(90)
    tr.fd(i)
    tr.left(90)
    tr.fd(i)
    tr.left(90)
    tr.penup()
    tr.goto((-50*i/100),(-50*i/100))
    tr.pendown()
tr.exitonclick()