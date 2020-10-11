import turtle_def_mnogoangles_9 as tr
import numpy as np
tr.speed(0)
tr.width(3)
tr.shape('turtle')
tr.turtlesize(1)
tr.color('plum')
for i in range(1,1800):
    tr.circle(10+i/(2*np.pi),1)
tr.exitonclick()
