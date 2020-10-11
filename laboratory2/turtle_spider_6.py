import turtle_def_mnogoangles_9 as tr

tr.shape('turtle')
tr.turtlesize(2)
tr.width(3)
tr.color('springgreen')
tr.goto(0,0)
for i in range(10):
    tr.fd(200)
    tr.stamp()
    tr.goto(0,0)
    tr.right(36)
tr.exitonclick()
