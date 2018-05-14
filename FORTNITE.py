#import pygame and turtle for dual windows
import pygame
#init for the text
pygame.init()
from turtle import *
#random for probability of surviving each encounter
from random import randint
#importing each quest file 
import QuestA
import QuestB
import QuestC
import QuestD
import QuestE
import QuestF
import QuestG
import QuestH
import QuestI
import QuestJ

#DISPLAYING MAP OF FORTNITE
bgTurtle = Turtle()
screenTurtle = bgTurtle.getscreen()
screenTurtle.bgpic("bgMap.gif")
screenTurtle.setup(1024.1240)

#INPUT FOR WHERE THE USER WANTS TO LAND
textTurtle = Turtle()
screenText = textTurtle.getscreen()
myDialogue = screenText.textinput("Fortnite", "Battle Bus is fueling. Waiting for players... Where would you like to land?")

#Link for code to display text
# https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
SIZE = WIDTH, HEIGHT = (1024, 720)
FPS = 30
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()


def blit_text(surface, text, pos, font, color=pygame.Color('red')):
    words = [word.split(' ') for word in text.splitlines()]  
    #2D array where each row is a list of words
    space = font.size(' ')[0]  
    #The width of a space
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                #Reset the x
                y += word_height  
                #Start on new row
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  
        #Reset the x
        y += word_height  
        #Start on new row

#Quest A is titled towers
if myDialogue == "tilted towers":
    QuestAA()

#Quest B is pleasant park
if myDialogue == "pleasant park":
    QuestBA()

#Quest C is shifty shafts
if myDialogue == "shifty shafts":
    QuestCA()

#Quest D is greasy grove
if myDialogue == "greasy grove":
    QuestDA()

#Quest E is snobby shores
if myDialogue == "snobby shores":
    QuestEA()
    
#QuestF is salty springs
if myDialogue == "salty springs":
    QuestFA()

#QuestG is retail row
if myDialogue == "retail row":
    QuestGA()

#QuestH is tomato town
if myDialogue == "tomato town":
    QuestHA()

#QuestI is anarchy acres
if myDialogue == "anarchy acres":
    QuestIA()

#QuestJ is loot lake
if myDialogue == "loot lake":
    QuestJA()

#font for the text
font = pygame.font.SysFont('Arial', 14)

while True:
    #Keeping text on screen
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    #Screen color
    screen.fill(pygame.Color('black'))
    blit_text(screen, text, (20, 20), font)
    pygame.display.update()

