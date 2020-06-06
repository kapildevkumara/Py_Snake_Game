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
inc_level = 5
snake_length = 10

screen_width  = (width  // unit_block)  * unit_block
screen_height = (height // unit_block) * unit_block

