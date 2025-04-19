import pygame
from pygame.locals import *

"""
A program which just ouputs mouse and keyboard events.
"q" quits the program.

Cursor must be inside the game window, and the game
window must have the focus to be responsive.
"""

gameOn = True

pygame.init() # initialize the game window
# pygame needs a window
screen = pygame.display.set_mode((500, 400), 0, 32) # define the window size and position
pygame.display.set_caption('Drawing - Press q to quit')
WHITE = (255, 255, 255)
screen.fill(WHITE)
count = 0
# sensitivity for mouse moves
# 1 = max sensitivity; larger numbers are less sensitive
sensitivity = 10

while gameOn:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print(event.key)
            if event.key == K_q:
                gameOn = False
        elif event.type == MOUSEMOTION:
            count += 1
            if (count % sensitivity == 0):
                count = 0
                print("you moved the mouse")
        elif event.type == MOUSEBUTTONUP:
            print("mouse button up")
        elif event.type == MOUSEBUTTONDOWN:
            print("mouse button down")
    screen.fill(WHITE)
