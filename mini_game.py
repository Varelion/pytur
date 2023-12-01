from turtle import *

# 1. Create a turtle that can move in 4 directions

#2. Have an end goal

# 3. Have visual representation of goal

# START
# Background Orange
# Draw Ocean
# Move turtle to starting position

#Pressed MOVE key?
	#Move turtle in that direction

	#Have we reached the goal?
		#Hide turtle and disable controls
		#Write "YOU WIN!" on-screen

		#END


bgcolor("#D2691E")
speed(0)
move_distance = 50
wide = window_width()/2
tall = window_height()/2
ocean_start = wide-wide/3
ocean_end = round(wide)
goal = ocean_start

def game_init():
	# Draws the ocean on the sand
	penup()
	color("blue")
	begin_fill()
	goto(ocean_start, tall)
	pendown()
	goto(ocean_end, tall)
	goto(ocean_end, -tall)
	goto(ocean_start, -tall)
	goto(ocean_start, tall)
	end_fill()

def move_to_starting_position():
	penup()
	goto(-wide+10,0)
	pendown()
	dot(15,"white")
	color("green")
	write("The egg has hatched!")
	shape("turtle")

def check_goal():
	turtle_position = xcor()
	global goal
	if goal < turtle_position:
		hideturtle()
		penup()
		goto(0,0)
		color("white")
		write("YOU WIN!")
		onkey(None, "Up")
		onkey(None, "Down")
		onkey(None, "Left")
		onkey(None, "Right")


game_init()
move_to_starting_position()

def move_up():
	setheading(90)
	forward(move_distance)
	check_goal()

def move_down():
	setheading(270)
	forward(move_distance)
	check_goal()

def move_left():
	setheading(180)
	forward(move_distance)
	check_goal()

def move_right():
	setheading(0)
	forward(move_distance)
	check_goal()

onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")


listen()
done()
