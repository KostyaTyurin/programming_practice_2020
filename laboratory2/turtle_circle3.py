import turtle as tr
tr.shape('turtle')
tr.color('dimgrey')
tr.width(5)
for i in range(1, 1000):
    tr.speed(0)
    tr.fd(1)
    tr.left((1-((1000-2)/1000))*180)
    tr.fd(1)
tr.exitonclick()
