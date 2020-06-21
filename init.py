# Import
import cv2 
import sys
import random
import numpy as np

# Globals
WIDTH = 600				# Display Resolution Width 
HEIGHT = 600			# Display Resolution Height
UNIT_BLOCK = 20			# Grid Size
PAUSE_TIME = 250		# Initial Pause Time 
MIN_TIME = 125			# Minimum Wait Time
INC_LEVEL = 5			# Increment Level
SNAKE_LENGTH = 10		# Snake Length
EXIT_KEY = 27 			# Escape Key
AI_MODE = 0				# A-Star Algorithm Mode (1) and Normal Mode (0)

GREEN = (0, 255, 0)		
RED = (0, 0, 255)		
LEFT = -1				
UP = -2					
RIGHT = 1				
DOWN = 2				

grid_x = (WIDTH  // UNIT_BLOCK)
grid_y = (HEIGHT // UNIT_BLOCK)

screen_width  = grid_x  * UNIT_BLOCK
screen_height = grid_y * UNIT_BLOCK
