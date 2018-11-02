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
random_seed = 7596
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
    size(w, h)

    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high

    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)

    # Set the number of frames per second to display
    frameRate(frame_rate)
    
    background(0, 0, 95)
    
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
    
    background(g.backgroundColor)
    
    noFill()
    stroke(0, 0, 25)
        
    r = 200

    translate(width/2, height/2)

    # Full bug
    w_bug = random(300, 600)
    h_bug = random(500, 800) # Calculate based on ratio (w_bug*random_multiplier)
    x_0 = 0-w_bug/2
    y_0 = 0-h_bug/2
    
    # Head
    x_head = x_0
    y_head = y_0
    w_head = w_bug # * 0.9
    h_head = random(h_bug*0.1, h_bug*0.2)

    # Pronotum
    x_pronotum = x_0
    y_pronotum = y_head + h_head
    w_pronotum = w_bug# * 0.9
    h_pronotum = random(h_head, h_bug*0.4)

    # Elytron
    x_elytron = x_0
    y_elytron = y_pronotum + h_pronotum
    w_elytron = w_bug# * 0.9
    h_elytron = h_bug - h_head - h_pronotum
    
    
    x = x_head+w_head*0.4/2
    y = y_head
    w = w_head-w_head*0.4
    h = h_head
    draw_head(x, y, w, h)
    
    x = x_elytron+w_elytron*0.2/2
    y = y_elytron
    w = w_elytron-w_elytron*0.2
    h = h_elytron
    draw_elytron(x, y, w, h)

    x = x_pronotum+w_pronotum*0.2/2
    y = y_pronotum
    w = w_pronotum-w_pronotum*0.2
    h = h_pronotum
    draw_pronotum(x, y, w, h)


    # curveTightness(0)
    # y_n, x_e, y_s, x_w = elytron(0, 100, r=200)
    # y_n, x_e, y_s, x_w = pronotum(0, y_n, r=100)
    
    helper.save_frame_timestamp('buggies', timestamp, random_seed)

    # Save memory by closing image, just look at it in the file system
    # if (w > 1000) or (h > 1000):
    #     exit()


################################################################################
# Functions
################################################################################

def draw_head(x, y, w, h):
    fill(0, 0, 30)
    #rect(x, y, w, h)
    beginShape()
    cv_point(x, y)
    cv_point(x+w, y)
    cv_point(x+w, y+h)
    cv_point(x, y+h)
    cv_point(x, y)
    cv_point(x+w, y)
    cv_point(x+w, y+h)
    endShape()
    
def draw_pronotum(x, y, w, h):
    fill(0, 0, 50)
    #rect(x, y, w, h)
    beginShape()
    cv_point(x, y)
    cv_point(x+w, y)
    cv_point(x+w, y+h)
    cv_point(x, y+h)
    cv_point(x, y)
    cv_point(x+w, y)
    cv_point(x+w, y+h)
    endShape()
    
def draw_elytron(x, y, w, h):
    w_squeeze = 50
    y_squeeze = 50
    
    fill(0, 0, 70)
    #rect(x, y, w, h)
    beginShape()
    cv_point(x, y)
    cv_point(x+w, y)
    cv_point(x+w-w_squeeze, y+h-y_squeeze)
    cv_point(x+w/2, y+h+50)
    cv_point(x+w_squeeze, y+h-y_squeeze)
    cv_point(x, y)
    cv_point(x+w, y)
    cv_point(x+w-w_squeeze, y+h-y_squeeze)
    endShape()

def cv_point(x, y):
    curveVertex(x, y)
    ellipse(x, y, 5, 5)

def mousePressed():
    helper.save_frame_timestamp('buggies', timestamp, random_seed)
    
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
