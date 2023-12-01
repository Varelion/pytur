from turtle import *

#  Start -> Draw Ballowwn -> up key pressed -> balloon at max size? pop : inflate -> clear balloon white "POP"!

balloon_diameter = 40
pop_diameter = 100

def draw_balloon():
	color("red")
	dot(balloon_diameter)

def inflate_balloon():
	global balloon_diameter
	balloon_diameter +=10
	if (balloon_diameter < pop_diameter):
		return draw_balloon()
	else:
		color("white")
		dot(balloon_diameter+1)
		return print("POP!")

def pop():
	return False

draw_balloon()

onkey(inflate_balloon, "space")
listen()

mainloop()
