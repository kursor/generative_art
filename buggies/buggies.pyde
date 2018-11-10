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
    #draw_pronotum(x, y, w, h)


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
    cvp(x, y)
    cvp(x+w, y)
    cvp(x+w, y+h)
    cvp(x, y+h)
    cvp(x, y)
    cvp(x+w, y)
    cvp(x+w, y+h)
    endShape()
    
def draw_pronotum(x, y, w, h):
    y_squeeze = y*random(0.01, 0.17)
    
    fill(0, 0, 50)
    #rect(x, y, w, h)
    beginShape()
    cvp(x, y)
    cvp(x+w/2, y+y_squeeze)
    cvp(x+w, y)
    cvp(x+w, y+h)
    cvp(x, y+h)
    cvp(x, y)
    cvp(x+w/2, y+y_squeeze)
    cvp(x+w, y)
    endShape()
    
def draw_elytron(x, y, w, h):
    w_squeeze = w*random(0.01, 0.2)
    y_squeeze = h*random(0.01, 0.4)
    

    
    # Body
    fill(0, 0, 70)
    beginShape()
    cvp(x*0.8, y)
    cvp(x+w*0.5, y*1.3)
    cvp(x*1.2+w, y)
    cvp(x+w-w_squeeze*1.2, y+h-y_squeeze)
    cvp(x+w/2, y+h*1.2)
    cvp(x+w_squeeze*1.2, y+h-y_squeeze)
    cvp(x*0.8, y)
    cvp(x+w*0.5, y*1.3)
    cvp(x*1.2+w, y)
    endShape()
    
    # Left wing cover
    fill(0, 0, 70)
    #rect(x, y, w, h)
    beginShape()
    cvp(x, y)
    cvp(x+w*0.25, y-50)
    cvp(x+w*0.5, y)
    curveTightness(0.4)
    cvp(x+w*0.5, y+h+50)
    curveTightness(0.9)
    cvp(x+w_squeeze, y+h-y_squeeze)
    curveTightness(0)
    cvp(x, y)
    cvp(x+w*0.25, y-50)
    cvp(x+w*0.5, y)
    endShape()
    
    # Right wing cover
    fill(0, 0, 70)
    #rect(x, y, w, h)
    beginShape()
    cvp(x+w*0.5, y)
    curveTightness(0.9)
    cvp(x+w*0.75, y-50)
    curveTightness(0.4)
    cvp(x+w, y)
    curveTightness(0)
    cvp(x+w-w_squeeze, y+h-y_squeeze)
    cvp(x+w*0.5, y+h+50)
    cvp(x+w*0.5, y)
    curveTightness(0.9)
    cvp(x+w*0.75, y-50)
    curveTightness(0.4)
    cvp(x+w, y)
    curveTightness(0)
    endShape()
    
    
    #FIXME USE PUSH POP MATRIX FOR ONE LEG THEN ROTATE
    
    
    # Shoulder
    beginShape()
    cvp(x+w*0.5, y+h*0.2)
    cvp(x-w*0.2, y+h*0.2)
    cvp(x-w*0.2, y+h*0.2)
    endShape()
    
    line(x+w*0.5, y+h*0.8, x-w*0.2, y+h*0.8)

def draw_upper_legs(x, y, w, h):
    # based off of body shape/position, shoulder, arm w/fuzz, 4 point triangles, claws
    pass
             
             
def cvp(x, y):
    curveVertex(x, y)
    ellipse(x, y, 5, 5)

def mousePressed():
    helper.save_frame_timestamp('buggies', timestamp, random_seed)
    
