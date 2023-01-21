
import turtle


pen = turtle.Turtle()


def curve():
	for i in range(200):

		
		pen.right(1)
		pen.forward(1)


def heart():

	
	pen.fillcolor('red')

	
	pen.begin_fill()

	
	pen.left(140)
	pen.forward(113)

	
	curve()
	pen.left(120)


	curve()

	# Draw the right line
	pen.forward(112)

	# Ending the filling of the color
	pen.end_fill()

# Defining method to write text
def txt():

	# Move turtle to air
	pen.up()

	# Move turtle to a given position
	pen.setpos(-68, 95)

	# Move the turtle to the ground
	pen.down()

	# Set the text color to lightgreen
	pen.color('lightgreen')

	# Write the specified text in
	# specified font style and size
	pen.write("love u", font=(
	"Verdana", 12, "bold"))


# Draw a heart
heart()

# Write text
txt()

# To hide turtle
pen.ht()
