################################################################################
# Aaron Penne
# https://github.com/aaronpenne
################################################################################

import datetime
import string
import sys
from random import shuffle, seed

import helper

################################################################################
# Global variables
################################################################################

random_seed = int(random(0, 10000))
random_seed = helper.get_seed(random_seed)
helper.set_seed(random_seed)

# Get time
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# Parameters for draw speed
frame_rate = 30

################################################################################
# Knobs to turn
################################################################################

# Canvas size
w = 1000  # width
h = 1000  # height

opacity = 20

divisions = 8

a_step = PI/100
angles_1 = helper.range_float(0, 3*(TWO_PI+a_step), a_step)
angles_2 = helper.range_float(0+TWO_PI/3, 3*(TWO_PI+TWO_PI/3+a_step), a_step)
angles_3 = helper.range_float(0+2*TWO_PI/3, 3*(TWO_PI+2*TWO_PI/3+a_step), a_step)

################################################################################
# setup()
# function gets run once at start of program
################################################################################

def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h)

    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high

    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)

    # Set the number of frames per second to display
    frameRate(frame_rate)
    
    background(0, 0, 100)
    
    # Stops draw() from running in an infinite loop (should be last line)
    #noLoop()  # Comment to run draw() infinitely (or until 'count' hits limit)


################################################################################
# draw()
# function gets run repeatedly (unless noLoop() called in setup())
################################################################################

def draw():
    
    a = angles_1[frameCount]
    stroke(180, 100, 100, opacity) # cyan
    x_circle, y_circle = helper.circle_points(w/2, h/2, 100, a)
    for row in range(1, divisions):
        for col in range(1, divisions):
            x = col * w/divisions
            y = row * h/divisions
            line(x, y, x_circle, y_circle)
        
    a = angles_2[frameCount]
    stroke(300, 100, 100, opacity) # magenta
    x_circle, y_circle = helper.circle_points(w/2, h/2, 100, a)
    for row in range(1, divisions):
        for col in range(1, divisions):
            x = col * w/divisions
            y = row * h/divisions
            line(x, y, x_circle, y_circle)
            
    a = angles_3[frameCount]
    stroke(60, 100, 100, opacity) # yellow
    x_circle, y_circle = helper.circle_points(w/2, h/2, 100, a)
    for row in range(1, divisions):
        for col in range(1, divisions):
            x = col * w/divisions
            y = row * h/divisions
            line(x, y, x_circle, y_circle)
            
    #helper.save_frame_timestamp('fuzz', timestamp, random_seed)

    # Save memory by closing image, just look at it in the file system
    # if (w > 1000) or (h > 1000):
    #     exit()


################################################################################
# Functions
################################################################################

def mousePressed():
    helper.save_frame_timestamp('fuzz', timestamp, random_seed)
