# Assigment 2:      Question 1 - Turtle draw
# Contributors:     Julio Del Cid studentid 332808
# GITHUB Repo:      https://github.com/JulioDelCid/SS20-HIT137-A2/ 
# Credits:          https://docs.python.org/3/library/turtle.html, 
#                   https://www.techwithtim.net/tutorials/python-module-walk-throughs/turtle-module/,
#                   https://www.youtube.com/watch?v=hxbEubm1yQo 
#
#############       Commence assignmet code ##############################


import turtle
from turtle  import Screen, Turtle

# Set up the environment and turtle
screen = Screen()
t = Turtle("turtle")
t.speed(-1)
t.pencolor('red')
t.color("red", "green")
t.pensize(5)

# Screen background colour and 
screen.bgcolor("grey")

# These parameters will be the mouse position
def mousedrag(x, y):  
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(mousedrag)


def clickRight():
    t.clear()
    
# This will run the program
def main():  
    turtle.listen()

    
# When we drag the turtle object call dragging
    t.ondrag(mousedrag) 
    turtle.onscreenclick(clickRight, 3)

# This prevents closing the program by continuing to run main() 
    screen.mainloop()  
main()