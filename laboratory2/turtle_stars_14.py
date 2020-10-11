import turtle as tr
tr.shape('turtle')
tr.speed(10)
tr.color('black')

for n in range(5,12,6):
    def angle(n):
        return 180 - ((n - 2) * 180 / (3 * n))

    for i in range(n):
        tr.left(angle(n))
        tr.fd(20 * n)

    tr.penup()
    tr.fd(300)
    tr.pendown()
tr.exitonclick()