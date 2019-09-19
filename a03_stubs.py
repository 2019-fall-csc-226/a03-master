
# TODO Do not edit this file directly! Instead, create a new file called
# TODO a03_username.py and copy this code into it!

#################################################################################
# Author:
# Username:
#
# Assignment:
# Purpose:
# Google Doc Link:
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################




import turtle
sc = turtle.Screen()
sc.bgcolor("#ADD8E6")
ht = turtle.Turtle()
ht.pensize(15)
ht.penup()
ht.setpos(-200, 0)
ht.pendown()
ht.speed(10)

def draw_square(ht):
    ht.fillcolor("#FFFF33")
    ht.begin_fill()
    for a in range(4):              #draws the main part of the house
         ht.fd(300)
         ht.right(90)
    ht.end_fill()

    pass
def drawtriangle(ht):
    ht.fillcolor("#ff0000")
    ht.begin_fill()
    for t in range(3):             #draws the roof of the house
        ht.fd(150)
        ht.left(120)
        ht.fd(150)
    ht.end_fill()
def drawwindow(ht):
    ht.fillcolor("#0000FF")
    ht.begin_fill()
    for w in range(4):
        ht.fd(100)
        ht.right(90)
    ht.end_fill()

    pass
def drawdoor(ht):
    ht.fillcolor("#D2691E")
    ht.begin_fill()
    ht.fd(50)
    ht.right(90)
    ht.forward(90)
    ht.right(90)
    ht.fd(100)
    ht.right(90)
    ht.fd(90)
    ht.right(90)
    ht.fd(80)
    ht.end_fill()
    ht.right(90)
    ht.penup()
    ht.fd(55)
def drawgrass(ht):      #Function to create grass underneath the house
    ht.setpos(-690, -315)
    ht.right(90)
    ht.pendown()
    ht.pencolor("#228B22")
    ht.fillcolor("#228B22")   #Changes the fill color to green
    ht.begin_fill()
    ht.fd(1500)
    ht.right(90)
    ht.fd(30)
    ht.right(90)
    ht.fd(1500)
    ht.right(90)
    ht.fd(30)
    ht.end_fill()
def stick(ht):
    ht.color("#000000")  #setting color and pensize for the stick figure
    ht.pensize(5)

    ht.left(120)   #draws the stick figure
    ht.fd(50)
    ht.right(120)
    ht.fd(55)
    ht.right(180)
    ht.fd(55)
    ht.right(30)
    ht.pendown()
    ht.fd(50)
    ht.right(45)
    ht.fd(50)
    ht.right(180)
    ht.fd(100)
    ht.left(180)
    ht.fd(50)
    ht.left(15)
    ht.fd(5)
    ht.circle(30)
def message(ht):
    ht.setpos(70, -20)     #tells turtle to write a message on the screen
    ht.color("#000000")
    style = ('Courier', 20, 'italic')
    ht.write("Hello, and Welcome to my Home!!!", font=style, )

def main():
    drawtriangle(ht)   #starts drawing the house, beginning with the roof
    ht.fd(150)
    ht.right(90)
    draw_square(ht)
    ht.fd(120)         #draws the main part of the house, and sets position of turtle
    ht.right(90)

    ht.penup()
    ht.fd(40)
    ht.pendown()          #positions the turtle and draws the window
    drawwindow(ht)
    ht.penup()
    ht.fd(120)
    ht.pendown()
    drawwindow(ht)           #draws the second window

    ht.penup()
    ht.setpos(-200, -300)       #postitions the turtle and draws a door
    ht.pendown()
    drawdoor(ht)
    drawgrass(ht)

    ht.penup()
    ht.right(90)
    ht.fd(1000)
    ht.left(90)
    ht.fd(10)
    ht.right(145)
    ht.pendown()
    stick(ht)
    ht.penup()
    ht.fd(50)
    message(ht)

                             #draws grass below the house




main()



sc.exitonclick()





