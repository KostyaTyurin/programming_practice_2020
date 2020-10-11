from random import randint
import turtle as tr
tr.shape('turtle')
tr.speed(10)
for n in range(randint(20,1000)):
    tr.fd(randint(10, 15))
    tr.left(randint(1, 180))