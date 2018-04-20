#THIS IS A FORTNITE CHOOSE YOUR OWN ADVENTURE GAME
#What's your project? FORTNITE CHOOSE YOUR OWN ADVENTURE.
#What is your first major milestone? A WORKING GAME.
#What do you not know that you will need to learn? RANDINT 
#In what ways is your project too ambitious? TOO DEEP ON EACH LANDING PLACE
#In what ways is it possibly not ambitious enough? WORK HARDER

from turtle import *
from random import randint

#DISPLAYING MAP OF FORTNITE
bgTurtle = Turtle()
screenTurtle = bgTurtle.getscreen()
screenTurtle.bgpic("map.gif")
screenTurtle.setup(1024.1240)

#INPUT FOR WHERE THE USER WANTS TO LAND
textTurtle = Turtle()

screenText = textTurtle.getscreen()

myDialogue = screenText.textinput("Fortnite", "Battle Bus is fueling. Waiting for players... Where would you like to land?")
#turtle.resetscreen()
#screenText.screensize(200,200)
#turtle.hideturtle()
#screenTurtle = bgTurtle.getscreen()
#screenTurtle.bgcolor("lightblue")
textTurtle.ht()
textTurtle.penup()
textTurtle.setpos(-100,100)
textTurtle.write(myDialogue, move = False, align="left", font=("Arial", 16, "normal"))



#IF THEY CHOOSE TO DROP TILTED
if myDialogue == "tilted towers":
    textTurtle.write("You land on a brick building and pick up a green pump shotgun.")
    #30% CHANCE OF DYING AND 70% CHANCE OF SURVIVING
    computerTilted = randint(1,10)
    if computerTilted > 3:
        textTurtle.write("Another player lands next to you and you quickly eliminate him with two shots. Good job!")
        
    else:
        textTurtle.write("Another player lands on the roof, breaks the ceiling, and one pumps you in the head with a shotgun.")
        textTurtle.write("You have been eliminated.")
        textTurtle.write("Sorry.")
        textTurtle.write("Please play again")
        done()


