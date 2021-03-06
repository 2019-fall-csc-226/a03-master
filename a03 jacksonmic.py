# Author: Micheala Jackson
# Username:Jacksonmic
#
# Assignment:A03
# Purpose:
# Google Doc Link:https://docs.google.com/document/d/1o_smJNzY5sSGsk20-J2YIMe9H120Xn4wQJXCWOjBRMU/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Azis, Will, and Christian helpped me with figuring out the right kind of code to creat things such as the chimney smoke and the roof of the house
#
#
#################################################################################

import turtle



def function_1(hse):  #the base of the house
    """
    This code make the initial foundation for the house
    """
    hse.begin_fill()
    for side in range(4):
        hse.pendown()
        hse.forward(270)
        hse.right(90)
        hse.penup()
    hse.end_fill()

    hse.begin_fill()
    pass
    # ...


def function_2(hse):
    """
    This function builds the roof of the house
    """
    for side in range(3):
       #draws the roof
        hse.color(136, 45, 0)
        # hse.left(45)
        hse.pendown()
        hse.forward(270)
        if side == 2:
            hse.left(60)
            break
        hse.left(120) #Azis and christian helped me figure out the angles needed to draw the roof so that it would do any weird turns
        # hse.forward(65)
        # hse.right(45)
    hse.end_fill()
    pass
    # ...
def function_3(hse):
 for side in range(1):   # draws the chimney
    hse.begin_fill()
    hse.color("blue")
    hse.pendown()
    hse.right(235)
    hse.forward(150)
    hse.left(118)
   # hse.right(45)
    #hse.left(45)
    hse.forward(75)
    hse.left(90)
    hse.forward(135)
    hse.end_fill()
    #hse.left()
    hse.penup()
    hse.left(180)
    hse.forward(145)
    hse.right(90)
    hse.pendown()

def function_4(hse): #makes chimney smoke
    for i in range(2):
        for i in range(25):
            # """"will helped me create the half circles needed to create the smoke out the chimney"""
            hse.color("gray")
            distance = 5
            angle = 2
            angle = angle + 5
            hse.forward(distance)
            hse.left(angle)
        hse.right(180)
    hse.penup()
    hse.setpos(270, -75)
    hse.left(190)
    hse.pensize(10)

def function_5(hse): #window build function
    for Win1 in range(4):
        """makes 2 windows"""

        #hse.right(90)
       # hse.left(180)
        hse.pendown()
        hse.forward(50)
        hse.left(90)
        hse.forward(50)
        hse.left(90)
    hse.forward(25)
    hse.left(90)
    hse.forward(25)
    hse.left(90)
    hse.forward(25)
    hse.left(180)
    hse.forward(50)
    hse.left(180)
    hse.forward(50)
    hse.right(90)
    hse.forward(25)
    hse.right(90)
    hse.forward(25)
    hse.left(270)
    hse.forward(25)
    hse.penup()
    hse.setpos(45, -125)
    hse.pendown()
    hse.forward(50)
    hse.left(90)
    hse.forward(50)
    hse.left(90)
    hse.forward(50)
    hse.left(90)
    hse.forward(45)
    hse.left(90)
    hse.forward(25)
    hse.left(90)
    hse.forward(40)
    hse.right(90)
    hse.forward(25)
    hse.right(90)
    hse.forward(20)
    hse.right(90)
    hse.forward(40)
    # hse.left(270)
    # hse.forward(25)
    hse.penup()


def function_6(hse):
    #builds the door
    hse.setpos(100, -145)
    hse.pendown()
    hse.left(90)
    for D in range(2):
        """This function builds the door
        """
        hse.forward(50)
        hse.right(90)
        hse.forward(120)
        hse.right(90)
        # hse.forward(50)



def main():
    """
    Docstring for main
    """
    # ...
    wn = turtle.Screen()
    wn.bgcolor("light blue")  # turns the background to light blue
    wn.colormode(255)
    hse = turtle.Turtle()
    hse.shape("turtle")
    hse.begin_fill()
    hse.color("yellow")
    # make the main house
    hse.pensize(15)
    hse.speed(0)

    function_1(hse)            # Function call to function_1
    function_2(hse)            # Function call to function_2
    function_3(hse)
    function_4(hse)
    function_5(hse)
    function_6(hse)
    wn.exitonclick()
main()


