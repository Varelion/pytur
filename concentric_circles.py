from turtle import *

# Initialize the variable that will serve as the first circle's starting point.
x = 200
# Create a loop, that says, as long as x is positive, run.
while x > 0:
    circle(x)
	# after running, we decrease the variable's size by 10
    x -= 10

done()
