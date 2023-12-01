from turtle import *
speed(0)
# Here we create a circle with a radius, not diameter, or 50 units.
circle (50)
penup()
forward(100)
pendown()
circle(50)
# Given radius is half a circle, by moving forward 100 units, the second radius circle is touching the first without overlap.
penup()
backward(100)
right(90)
forward(35)
pendown()
circle(50)

done()
