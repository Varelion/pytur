# Black background, different colored planets.

from turtle import *

# Draws instantly
speed(0)
# Black background
bgcolor("black")

# Draws sun
begin_fill()
color("orange")
circle(60)
end_fill()

# moves
penup()
forward(100)

# creates mercury
pendown()
begin_fill()
color("grey")
circle(20)
end_fill()

# moves
penup()
forward(80)

# Creates venus
pendown()
begin_fill()
color("red")
circle(40)
end_fill()

# moves
penup()
forward(120)

# creates earth
pendown()
begin_fill()
color("green")
circle(30)
end_fill()

done()
