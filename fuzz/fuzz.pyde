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

opacity = 3

divisions = 6

a_step = PI/100
angles_1 = helper.range_float(0, 3*(TWO_PI+a_step), a_step)
angles_2 = helper.range_float(0+TWO_PI/3, 3*(TWO_PI+TWO_PI/3+a_step), a_step)
angles_3 = helper.range_float(0+2*TWO_PI/3, 3*(TWO_PI+2*TWO_PI/3+a_step), a_step)

angles_1 = [random(x, x+a_step) for x in angles_1]
angles_2 = [random(x, x+a_step) for x in angles_2]
angles_3 = [random(x, x+a_step) for x in angles_3]

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
    
    background(0, 0, 25)
    
    # Stops draw() from running in an infinite loop (should be last line)
    #noLoop()  # Comment to run draw() infinitely (or until 'count' hits limit)


################################################################################
# draw()
# function gets run repeatedly (unless noLoop() called in setup())
################################################################################

def draw():
    noFill()
    
    background(0, 0, 25)
    
    stroke(342, 32, 85)
    a = angles_1[frameCount]
    #stroke(180, 100, 100, opacity) # cyan
    #stroke(16.3, 28.6, 96.1) # salmon
    x_circle, y_circle = helper.circle_points(w/2, h/2, 100, a)
    for row in range(1, divisions):
        for col in range(1, divisions):
            strokeWeight(random(1, 5))
            x = col * w/divisions
            y = row * h/divisions
            beginShape()
            curveVertex(x, y) 
            curveVertex(x, y)
            for idx in range(3):
                x_rand = random(x, x_circle)
                y_rand = random(y, y_circle)
                curveVertex(x_rand, y_rand)
            curveVertex(x_circle, y_circle)
            curveVertex(x_circle, y_circle)
            endShape()
            
    stroke(41, 41, 66)
    a = angles_2[frameCount]
    #stroke(180, 100, 100, opacity) # cyan
    #stroke(16.3, 28.6, 96.1) # salmon
    x_circle, y_circle = helper.circle_points(w/2, h/2, 100, a)
    for row in range(1, divisions):
        for col in range(1, divisions):
            strokeWeight(random(1, 5))
            x = col * w/divisions
            y = row * h/divisions
            beginShape()
            curveVertex(x, y)
            curveVertex(x, y)
            for idx in range(3):
                x_rand = random(x, x_circle)
                y_rand = random(y, y_circle)
                curveVertex(x_rand, y_rand)
            curveVertex(x_circle, y_circle)
            curveVertex(x_circle, y_circle)
            endShape()
        
    stroke(98, 19, 87)    
    a = angles_3[frameCount]
    #stroke(180, 100, 100, opacity) # cyan
    #stroke(16.3, 28.6, 96.1) # salmon
    x_circle, y_circle = helper.circle_points(w/2, h/2, 100, a)
    for row in range(1, divisions):
        for col in range(1, divisions):
            strokeWeight(random(1, 5))
            x = col * w/divisions
            y = row * h/divisions
            beginShape()
            curveVertex(x, y)
            curveVertex(x, y)
            for idx in range(3):
                x_rand = random(x, x_circle)
                y_rand = random(y, y_circle)
                curveVertex(x_rand, y_rand)
            curveVertex(x_circle, y_circle)
            curveVertex(x_circle, y_circle)
            endShape()
            
            
    #helper.save_frame_timestamp('fuzz', timestamp, random_seed)

    # Save memory by closing image, just look at it in the file system
    # if (w > 1000) or (h > 1000):
    #     exit()


################################################################################
# Functions
################################################################################

def mousePressed():
    helper.save_frame_timestamp('fuzz', timestamp, random_seed)
