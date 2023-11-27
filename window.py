import pygame, sys, time
from pygame.locals import *
import random

# Set up pygame
pygame.init()

# Set up the window
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('TripGenerator')

# Set up directional variables
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

MOVESPEED = 4

counter_duration = 2000  # 2 seconds
counter_start_time = pygame.time.get_ticks()
reset_duration = 4000 # 4 seconds

# Colors (RGB)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (75, 0, 130)

# Set up the box data structures (dictionaries to store dimensions, color, and direction of each box)
b1 = {'rect': pygame.Rect(0, 250, 3, 3), 'color': BLUE, 'dir': LEFT}
b2 = {'rect': pygame.Rect(500, 250, 3, 3), 'color': BLACK, 'dir': UPRIGHT}


boxes = [b1, b2]  # List of the box data structures (to iterate through in the loop)

# Run the game loop
while True:
    # Check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # collision detection
    for b in boxes:
        # Move the box data structure
        if b['dir'] in {UPLEFT, UPRIGHT, UP}:
            b['rect'].top -= MOVESPEED
        elif b['dir'] in {DOWNLEFT, DOWNRIGHT, DOWN}:
            b['rect'].top += MOVESPEED
        if b['dir'] in {UPLEFT, DOWNLEFT, LEFT}:
            b['rect'].left -= MOVESPEED
        elif b['dir'] in {UPRIGHT, DOWNRIGHT, RIGHT}:
            b['rect'].left += MOVESPEED

        # Check if the box has moved out of the window and handle reflection
        if b['rect'].top < 0:
            # Box has moved past the top
            b['dir'] = DOWNLEFT if b['dir'] == UPLEFT else DOWNRIGHT
        elif b['rect'].bottom > WINDOWHEIGHT:
            # Box has moved past the bottom
            b['dir'] = UPLEFT if b['dir'] == DOWNLEFT else UPRIGHT

        if b['rect'].left < 0:
            # Box has moved past the left side
            b['dir'] = DOWNRIGHT if b['dir'] == DOWNLEFT else UPRIGHT
        elif b['rect'].right > WINDOWWIDTH:
            # Box has moved past the right side
            b['dir'] = DOWNLEFT if b['dir'] == DOWNRIGHT else UPLEFT

        # Check the counter and modify the box behavior after 2 seconds
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - counter_start_time
        if elapsed_time >= counter_duration:
            b1['color'] = BLUE
            b2['color'] = BLACK

        # Check if the box color should be reset to white after 2 seconds
        if elapsed_time >= reset_duration:

            b1['color'] = random.choice([RED, GREEN, BLUE, PURPLE, WHITE, BLACK])
            b2['color'] = random.choice([RED, GREEN, BLUE, PURPLE, WHITE, BLACK])

            # Restart the counter
            counter_start_time = pygame.time.get_ticks()

        # Draw the box onto the surface
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    # Draw the window onto the screen
    pygame.display.update()

    # Pause the program
    time.sleep(0.0000003)
