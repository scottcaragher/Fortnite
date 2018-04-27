import pygame
pygame.init()
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

#Link for code to display text
# https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
SIZE = WIDTH, HEIGHT = (1024, 720)
FPS = 30
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()


def blit_text(surface, text, pos, font, color=pygame.Color('red')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

if myDialogue == "tilted towers":
    text = "You land on a brick building and pick up a green pump shotgun."
    #30% CHANCE OF DYING AND 70% CHANCE OF SURVIVING
    computerTilted = randint(1,10)
    if computerTilted > 3:
        text = "Another player lands next to you and you quickly eliminate him with two shots. Good job!"
        
    else:
        text = "Another player lands on the roof, breaks the ceiling, and one pumps you in the head with a shotgun."
        text = "You have been eliminated."
        text = "Sorry."
        text = "Please play again"
        done()


font = pygame.font.SysFont('Arial', 14)

while True:

    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(pygame.Color('black'))
    blit_text(screen, text, (20, 20), font)
    pygame.display.update()

import QuestOne
QuestOne()