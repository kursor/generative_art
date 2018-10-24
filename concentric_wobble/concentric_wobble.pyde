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

opacity = 3

divisions = 10

a_step = PI/divisions
angles_1 = helper.range_float(0, TWO_PI, a_step)
a_step = PI/divisions
angles_2 = helper.range_float(0+TWO_PI/3, TWO_PI+TWO_PI/3, a_step)
a_step = PI/divisions
angles_3 = helper.range_float(0+2*TWO_PI/3, TWO_PI+2*TWO_PI/3, a_step)

offset = w*.005
offset_1 = [random(-offset, offset) for x in angles_1]
offset = w*.005 
offset_2 = [random(-offset, offset) for x in angles_2]
offset = w*.005 
offset_3 = [random(-offset, offset) for x in angles_3]

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
    step = 20
    # if frameCount == step*2:
    #     exit()
    
    counter = frameCount * PI/step
    
    background(0, 0, 25)
    noFill()
        
    x_center = w/2
    y_center = h/2
    
    print(frameCount) 
    
    # offset = [x*sin(counter) for x in offset_1]
    # draw_concentric_wobble(2, 50, int(w*0.3), 0.01, offset, angles_1, w/2, h/2)
        
        
    stroke(60, 7, 86)
    angles = [x+counter/2 for x in angles_1]
    offset = [x*sin(counter) for x in offset_1]
    draw_concentric_wobble(1, 2, int(w*0.4), 0.01, offset_1, angles_1, w/2, h/2) #1*w/3 
    
    angles = [x+counter/2 for x in angles_2]
    offset = [x*sin(counter) for x in offset_2]
    draw_concentric_wobble(1, 2, int(w*0.4), 0.01, offset_2, angles_2, w/2+frameCount, h/2) #1*w/3 
    
    angles = [x+counter/2 for x in angles_3]
    offset = [x*sin(counter) for x in offset_3]
    draw_concentric_wobble(1, 2, int(w*0.4), 0.01, offset_2, angles_2, w/2-frameCount, h/2) #1*w/3 
       
       
    #helper.save_frame_timestamp('concentric_wobble', timestamp, random_seed)

    # Save memory by closing image, just look at it in the file system
    # if (w > 1000) or (h > 1000):
    #     exit()


################################################################################
# Functions
################################################################################

def mousePressed():
    helper.save_frame_timestamp('concentric_wobble', timestamp, random_seed)
    
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
