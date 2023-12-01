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
move_distance = 20
wide = window_width()/2
tall = window_height()/2

def game_init():
	# Draws the ocean on the sand
	penup()
	color("blue")
	begin_fill()
	goto(round(wide-wide/3), tall)
	pendown()
	goto(round(wide), tall)
	goto(round(wide), -tall)
	goto(round(wide-wide/3), -tall)
	goto(round(wide-wide/3), tall)
	end_fill()

def move_turtle():
	penup()
	goto(-wide+10,0)
	pendown()
	dot(15,"white")
	color("green")
	write("The egg has hatched!")

game_init()
move_turtle()
done()
