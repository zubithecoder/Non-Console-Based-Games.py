# This is a simple café management (non-console-based) game using Pygame.

# Making a café management game using Pygame

import pygame
# pygame is a game development library for Python. / pygame → game engine.
import sys
# sys is a module that provides access to some variables used or maintained by the interpreter. / sys → system. / sys → lets us exit the program properly.

# -----------------------
# INITIAL SETUP
# -----------------------

pygame.init()
# pygame.init() initializes all the Pygame modules. (initialize means to set up or prepare something for use)
# This turns on all Pygame systems. (graphics, sound, keyboard, mouse)

WIDTH, HEIGHT = 800, 600
# Set the width and height of the game window. / A window 900x600 pixels.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# screen is the surface where everyone in the game will be drawn.
# pygame.display.set_mode() creates a window of the specified size.
pygame.display.set_caption("Cozy Café")
# pygame.display.set_caption() sets the title of the game window to "Cozy Café".

clock = pygame.time.Clock()
# clock controls FPS (frames per second) in the game. / FPS is how many times the screen updates per second.
FONT = pygame.font.SysFont("arial", 28)
# pygame.font.SysFont() creates a font object for rendering text. / "arial" is the font type, 28 is the size. (rendering means drawing text on the screen)
# This font will be used to display text in the game. / Font is used to draw text.

# Colors
WHITE = (255, 255, 255)
# WHITE color in RGB format. 
# RGB stands for Red, Green, Blue. 
# 255 is the maximum value for each color component. (means full intensity)
# white is used for background and text.
BROWN = (181, 101, 29)
# BROWN color in RGB format. 
# brown is used for buttons and café elements.
# 181 is the red component, 101 is the green component, 29 is the blue component.
LIGHT_BROWN = (222, 184, 135)
# LIGHT_BROWN color in RGB format.
# light brown is used for buttons and café elements.
# 222 is the red component, 184 is the green component, 135 is the blue component.
BLACK = (0, 0, 0)
# BLACK color in RGB format.
# black is used for text and outlines.
# 0 means no intensity for each color component.
GREEN = (100, 200, 100)
# GREEN color in RGB format.
# green is used for success messages and highlights.
# 100 is the red component, 200 is the green component, 100 is the blue 