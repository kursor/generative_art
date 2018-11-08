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
# random_seed = 7596
random_seed = helper.get_seed(random_seed)
helper.set_seed(random_seed)

# Get time
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# Parameters for draw speed
frame_rate = 2


################################################################################
# Knobs to turn
################################################################################

c_background = [13, 78, 76]


################################################################################
# setup()
# function gets run once at start of program
################################################################################

def setup():
    
    # Sets size of canvas in pixels (must be first line)
    size(1000, 1000)

    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high

    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)

    # Set the number of frames per second to display
    frameRate(frame_rate)
    
    background(*c_background)
    
    rectMode(CORNER)
    
    # Stops draw() from running in an infinite loop (should be last line)
    noLoop()  # Comment to run draw() infinitely (or until 'count' hits limit)


################################################################################
# draw()
# function gets run repeatedly (unless noLoop() called in setup())
################################################################################

def draw():
    step = 20
    # if frameCount == step*2:
    #     exit()
    
    counter = frameCount
    
    background(0, 0, 0)
    draw_background(width/2, height/2)
    
    noFill()
    stroke(0, 0, 25)
        
    r = 200

#     pushMatrix()
#     translate(width/2, 2*height/3)
#     draw_head(0, 0, 300, 230)
#     popMatrix()
    
    helper.save_frame_timestamp('creatures', timestamp, random_seed)

    # Save memory by closing image, just look at it in the file system
    # if (w > 1000) or (h > 1000):
    #     exit()


################################################################################
# Functions
################################################################################

def cvp(x, y):
    curveVertex(x, y)
    ellipse(x, y, 5, 5)

def mousePressed():
    helper.save_frame_timestamp('creatures', timestamp, random_seed)

def draw_head(x, y, w, h):
    fill(0, 0, 30)
    #rect(x, y, w, h)
    beginShape()
    cvp(x-w, y-h)
    cvp(x, y-h)
    cvp(x+w, y-h)
    cvp(x+w, y)
    cvp(x+w, y+h)
    cvp(x, y+h)
    cvp(x-w, y+h)
    cvp(x-w, y)
    cvp(x-w, y-h)
    cvp(x, y-h)
    cvp(x+w, y-h)
    endShape()
    
def draw_background(x=0, y=0):
    noStroke()
    radius = width
    h = c_background[0]
    for r in reversed(range(0, radius, 2)):
        fill(h, 78, 76)
        ellipse(x, y, r, r)
        h = h + 20*sin(PI+0.1*r)
