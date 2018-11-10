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

p_head_width = None
p_head_height = None
p_eye_distance = None

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
    imageMode(CENTER)
    
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
    
    translate(width/2, height/2)

    #draw_background(0, 0)
    draw_body(0, 100, width*1.2, height*0.8)
    
        
    r = 200

    draw_head(0, 200, 300, 230)
    
    draw_eyes(0, 200)
    
    draw_fur()
    draw_hairs()
    
    draw_horns(-300, 100, -350, -100, 10)
    draw_horns(300, 100, 350, -100, 10)
    
    draw_horns(-100, 50, -130, -200, 10)
    draw_horns(100, 50, 130, -200, 10)
    
    helper.save_frame_timestamp('creatures', timestamp, random_seed)

    # Save memory by closing image, just look at it in the file system
    # if (w > 1000) or (h > 1000):
    #     exit()


################################################################################
# Functions
################################################################################

def cvp(x, y):
    curveVertex(x, y)
    #ellipse(x, y, 5, 5)

def mousePressed():
    helper.save_frame_timestamp('creatures', timestamp, random_seed)

def draw_head(x, y, w, h):
    fill(0, 0, 30)
    #rect(x, y, w, h)
    
    top_offset = random(0, 100)
    bottom_offset = random(0, 100)
    side_offset = random(0, 100)
    
    beginShape()
    cvp(x-w, y-h)
    cvp(x, y-h-top_offset)
    cvp(x+w, y-h)
    cvp(x+w+side_offset, y)
    cvp(x+w, y+h)
    cvp(x, y+h+bottom_offset)
    cvp(x-w, y+h)
    cvp(x-w-side_offset, y)
    cvp(x-w, y-h)
    cvp(x, y-h-top_offset)
    cvp(x+w, y-h)
    endShape()
    
    
def draw_eyes(x, y):
    noStroke()
    fill(0, 0, 80)
    
    x_offset = random(0, 100)+20
    y_offset = random(0, 100)+20
    w = random(50, 100)
    h = random(50, 100)
    
    ellipse(x-x_offset, y-y_offset, w, h)
    ellipse(x+x_offset, y-y_offset, w, h)
    
    fill(0, 0, 0)
    x_offset = x_offset + random(-10, 10)
    y_offset = y_offset + random(-10, 10)
    w = w*0.2
    h = h*0.2
    ellipse(x-x_offset, y-y_offset, w, h)
    ellipse(x+x_offset, y-y_offset, w, h)
    
    
def draw_fur():
    pass
    
    
def draw_hairs():
    pass
    
def draw_body(x, y, w, h):
    body = createGraphics(width, height)
    body.colorMode(HSB, 360, 100, 100, 100)
    body.beginDraw()
    body.noStroke()
    body.translate(width/2, height/2)
    body.fill(color(0, 0, 20))
    body.ellipse(x, y, w, h)
    body.endDraw()
    body.filter(BLUR, 5)
    image(body, x, y)
    
def draw_horns(x1, y1, x2, y2, n):
    stroke(0, 0, 0)
    noFill()
    
    mid = (x2-x1)/2
    for i in range(n):
        x1_ = x1 + random(-3, 3)
        x2_ = x2 + random(-3, 3)
        y1_ = y1 + random(-3, 3)
        y2_ = y2 + random(-3, 3)
        beginShape()
        offset = random(-5, 5)
        cvp(x1_, y1_+offset)
        cvp(x1_, y1_+offset)
        offset = random(-5, 5)
        cvp(x1_+mid-mid/2, y1_+offset)
        offset = random(-5, 5)
        cvp(x1_+mid, y1_+offset)
        offset = random(-5, 5)
        cvp(x1_+mid+mid/2, y1_+offset)
        offset = random(-5, 5)
        cvp(x2_, y2_+offset)
        cvp(x2_, y2_+offset)
        endShape()
    
    
def draw_background(x=0, y=0):
    noStroke()
    radius = width
    h = c_background[0]
    for r in reversed(range(0, 2*width, 5)):
        fill(h, 78, 76)
        ellipse(x, y, r, r)
        h = h + 1*sin(PI+0.1*r)
