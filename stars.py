from random import *
from turtle import *

# black background, white stars
# Create random star size, in random location
# use a for loop to generate the above

# START

# Set background to BLACK
# Repeat 100 times
	# Generate random star position
	# Generate random star size
	# draw the star
# END
bgcolor("Black")
hideturtle()
speed(0)

MAXIMUM_STARS = 100
# window height and window width
width = window_width()
height = window_height()

def draw_star(xpos,ypos):
	star_size = randrange(1,30)
	penup()
	goto(xpos, ypos)
	pendown()
	dot(star_size, "white")

for x in range(MAXIMUM_STARS):
	xpos = randrange(round(-(width/2)),width)
	ypos = randrange(round(-(height/2)),height)
	draw_star(xpos, ypos)
	if x == MAXIMUM_STARS:
		print("Done!")
		done()


