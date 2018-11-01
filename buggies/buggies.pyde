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
#random_seed = 7263
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

    translate(w/2, h/2)

    # Full bug
    w_bug = random(300, 600)
    h_bug = random(500, 800) # Calculate based on ratio (w_bug*random_multiplier)
    x_0 = 0-w_bug/2
    y_0 = 0-h_bug/2
    
    # Head
    fill(0, 0, 30)
    x_head = x_0
    y_head = y_0
    w_head = w_bug # * 0.9
    h_head = random(h_bug*0.1, h_bug*0.2)
    rect(x_head, y_head, w_head, h_head)
    
    # Pronotum
    fill(0, 0, 50)
    x_pronotum = x_0
    y_pronotum = y_head + h_head
    w_pronotum = w_bug# * 0.9
    h_pronotum = random(h_head, h_bug*0.4)
    rect(x_pronotum, y_pronotum, w_pronotum, h_pronotum)

    # Elytron
    fill(0, 0, 70)
    x_elytron = x_0
    y_elytron = y_pronotum + h_pronotum
    w_elytron = w_bug# * 0.9
    h_elytron = h_bug - h_head - h_pronotum
    rect(x_elytron, y_elytron, w_elytron, h_elytron)


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

def pronotum(x_m, y_m, r=100):
    x_w = x_m - r/2
    x_e = x_m + r/2
    y_n = y_m - r
    y_s = y_m + r
    
    fill(0, 0, 30)
    
    beginShape()
    # north
    cv_point(x_m, y_n-r*0.2)
    # northeast
    cv_point(x_e, y_n)
    # east
    cv_point(x_e, y_m)
    # southeast
    #cv_point(x_e, y_s)
    # south
    cv_point(x_m, y_s+r*0.3)
    # southwest
    cv_point(x_w, y_s)
    # west
    cv_point(x_w, y_m)
    # northwest
    cv_point(x_w, y_n)
    # north
    cv_point(x_m, y_n-r*0.2)
    # northeast
    cv_point(x_e, y_n)
    # east
    cv_point(x_e, y_m)
    endShape()
    
    return y_n, x_e, y_s, x_w

def elytron(x_m, y_m, r=200):
    mouse_norm_x = 0.5 # map(mouseX, 0, w, -4, 0.8)

    fill(0, 0, 25)

    x_w = x_m - r/2
    x_e = x_m + r/2
    y_n = y_m - r
    y_s = y_m + r
    
    beginShape()
    # north
    cv_point(x_m, y_n-r*0.2)
    # northeast
    cv_point(x_e, y_n)
    # east
    cv_point(x_e, y_m)
    # southeast
    #cv_point(x_e, y_s)
    # south
    cv_point(x_m, y_s+r*0.3)
    # southwest
    curveTightness(mouse_norm_x)
    #cv_point(x_w, y_s)
    # west
    cv_point(x_w, y_m)
    # northwest
    cv_point(x_w, y_n)
    # north
    curveTightness(0)
    cv_point(x_m, y_n-r*0.2)
    # northeast
    cv_point(x_e, y_n)
    # east
    cv_point(x_e, y_m)
    endShape()
    
    return y_n, x_e, y_s, x_w

def cv_point(x, y):
    curveVertex(x, y)
    #ellipse(x, y, 5, 5)

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
