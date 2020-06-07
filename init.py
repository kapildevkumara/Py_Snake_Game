# Import
import cv2 
import sys
import random
import numpy as np

# Globals
width = 600
height = 600
unit_block = 20
pause_time = 250
min_time = 125
inc_level = 5
snake_length = 10
GREEN = (0, 255, 0)
RED = (0, 0, 255)
LEFT = -1
UP = -2
RIGHT = 1
DOWN = 2
EXIT_KEY = 27 # Escape Key
AI_MODE = 0

screen_width  = (width  // unit_block)  * unit_block
screen_height = (height // unit_block) * unit_block


