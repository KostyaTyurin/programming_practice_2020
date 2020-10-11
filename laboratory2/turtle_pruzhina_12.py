import turtle as tr
tr.shape('turtle')
tr.speed(6)
tr.color('black')
radius = 20
tr.left(90)
tr.penup()
tr.hideturtle()
tr.goto(-300, 0)
tr.pendown()
tr.showturtle()
for i in range(10):
    tr.circle(-50, 180)
    tr.circle(-5, 180)
tr.exitonclick()
