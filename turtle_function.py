from turtle import *

def move_and_turn(distance, angle):
	print("Going forward by ", distance, ".")
	forward(distance)
	print("Turning ", angle, " degrees.")
	right(angle)

move_and_turn(100, 45)
move_and_turn(44,4)

done()
