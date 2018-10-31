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
random_seed = 1138
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


################################################################################
# setup()
# function gets run once at start of program
################################################################################

def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h, P3D)

    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high

    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)

    # Set the number of frames per second to display
    frameRate(frame_rate)
    
    background(0, 0, 25)
    
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
    
    background(0, 0, 25)
    fill(0, 0, 95)
    stroke(0, 0, 25)
        
    r = 50
    x0 = w/2
    y0 = h/2
    
    rotateX(PI/8)
    
    translate(x0, y0)
    box(100)

       
    helper.save_frame_timestamp('urbie', timestamp, random_seed)

    # Save memory by closing image, just look at it in the file system
    # if (w > 1000) or (h > 1000):
    #     exit()


################################################################################
# Functions
################################################################################

def mousePressed():
    helper.save_frame_timestamp('urbie', timestamp, random_seed)
    
def draw_concentric_wobble(stroke_weight, r_start, r_end, r_offset, offset_list, angles_list, x_center, y_center):
    strokeWeight(stroke_weight)
        
    for r in range(r_start, r_end, 3*stroke_weight):
        offset = [r_offset*r*x for x in offset_list]
        #offset = [x for x in offset_list]
        
        beginShape()
        x_0, y_0 = helper.circle_points(x_center, y_center, r, angles_list[0])
        curveVertex(x_0 + offset[0], y_0 + offset[0])
        x_1, y_1 = helper.circle_points(x_center, y_center, r, angles_list[1])
        curveVertex(x_1 + offset[1], y_1 + offset[2])
        x_2, y_2 = helper.circle_points(x_center, y_center, r, angles_list[2])
        curveVertex(x_2 + offset[2], y_2 + offset[2])
        
        for idx,a in enumerate(angles_list[3:-1]):
            # radius = random_centered(radius, 30) # Randomize the radius a bit for each point
            x, y = helper.circle_points(x_center, y_center, r, a)
            curveVertex(x + offset[2+idx], y + offset[2+idx])
    
        # Run the curve through the starting three points to ensure smooth connection at the end
        curveVertex(x_0 + offset[0], y_0 + offset[0])
        curveVertex(x_1 + offset[1], y_1 + offset[2])
        curveVertex(x_2 + offset[2], y_2 + offset[2])
        endShape()
