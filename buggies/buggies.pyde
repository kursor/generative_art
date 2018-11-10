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
random_seed = 7598
random_seed = helper.get_seed(random_seed)
helper.set_seed(random_seed)

# Get time
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# Parameters for draw speed
frame_rate = 2

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
#
# 0--1--2--3--4
# |           |
# 15          5
# |           |
# 14          6
# |           |
# 13          7
# |           |
# 12-11-10--9-8
#
#
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
    y_gap = 20
    x_pron = x_0
    y_pron = y_head + h_head + y_gap
    w_pron = w_bug# * 0.9
    h_pron = random(h_head, h_bug*0.4)

    # Elytron
    y_gap = 20
    x_elyt = x_0
    y_elyt = y_pron + h_pron + y_gap
    w_elyt = w_bug# * 0.9
    h_elyt = h_bug - h_head - h_pron
    
    
    fill(0, 0, 50)
    head = get_16_points(x_head, y_head, w_head, h_head)

    pron = get_16_points(x_pron, y_pron, w_pron, h_pron)

    elyt = get_16_points(x_elyt, y_elyt, w_elyt, h_elyt)
    
    l_wing = get_16_points(elyt[0][0], elyt[0][1], w_elyt/2, h_elyt)
    
    r_wing = get_16_points(elyt[2][0], elyt[2][1], w_elyt/2, h_elyt)
    
    ################################################################################
    # Head
    ################################################################################         
    beginShape()
    cvp(*head[2])
    cvp(*head[8])
    cvp(*head[10])
    cvp(*head[12])
    cvp(*head[2])
    cvp(*head[8])
    cvp(*head[10])
    endShape()
    
    ################################################################################
    # Elytron
    ################################################################################         
    beginShape()
    cvp(*elyt[0])
    cvp(*elyt[2])
    cvp(*elyt[4])
    cvp(*elyt[7])
    cvp(*elyt[10])
    cvp(*elyt[13])
    cvp(*elyt[0])
    cvp(*elyt[2])
    cvp(*elyt[4])
    endShape()
    
    # ################################################################################
    # # Wing Coverings
    # ################################################################################         
    # # Left wing
    # pushMatrix()
    # #rotate(PI/4)
    # beginShape()
    # cvp(*elyt[0])
    # cvp(*elyt[1])
    # cvp(*elyt[2])
    # cvp(*elyt[10])
    # cvp(*elyt[13])
    # cvp(*elyt[0])
    # cvp(*elyt[1])
    # cvp(*elyt[2])
    # endShape()
    # popMatrix()
    
    # # Right wing
    # pushMatrix()
    # #rotate(PI/4)
    # beginShape()
    # cvp(*elyt[2])
    # cvp(*elyt[3])
    # cvp(*elyt[4])
    # cvp(*elyt[7])
    # cvp(*elyt[10])
    # cvp(*elyt[2])
    # cvp(*elyt[3])
    # cvp(*elyt[4])
    # endShape()
    # popMatrix()
    
    # ################################################################################
    # # Pronotum
    # ################################################################################         
    # beginShape()
    # cvp(*pron[0])
    # cvp(*pron[2])
    # cvp(*pron[4])
    # cvp(*pron[7])
    # cvp(*pron[10])
    # cvp(*pron[13])
    # cvp(*pron[0])
    # cvp(*pron[2])
    # cvp(*pron[4])
    # endShape()

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
             

             
             
def cvp(x, y):
    curveVertex(x, y)
    ellipse(x, y, 5, 5)
    
    
def get_16_points(x, y, w, h):
    points = [0]*16
    points[0] = [x, y]
    points[1] = [x+w*0.25, y]
    points[2] = [x+w*0.5, y]
    points[3] = [x+w*0.75, y]
    points[4] = [x+w, y]
    points[5] = [x+w, y+h*0.25]
    points[6] = [x+w, y+h*0.5]
    points[7] = [x+w, y+h*0.75]
    points[8] = [x+w, y+h]
    points[9] = [x+w*0.75, y+h]
    points[10] = [x+w*0.5, y+h]
    points[11] = [x+w*0.25, y+h]
    points[12] = [x, y+h]
    points[13] = [x, y+h*0.75]
    points[14] = [x, y+h*0.5]
    points[15] = [x, y+h*0.25]
    return points
    
    
def draw_16_points(points):
    beginShape()
    for p in points+points[0:3]:
        cvp(*p)
    endShape()
    
    
def draw_12_points(points):
    #points = [points[i] for i in [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15]]
    curveTightness(0.3)
    beginShape()
    for p in points+points[0:3]:
        cvp(*p)
    endShape()
    

def mousePressed():
    helper.save_frame_timestamp('buggies', timestamp, random_seed)
    
