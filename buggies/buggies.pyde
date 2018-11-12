##########################################################################
# Aaron Penne
# https://github.com/aaronpenne
##########################################################################

import datetime
import string
import sys
from random import shuffle, seed

import helper

##########################################################################
# Global variables
##########################################################################

random_seed = int(random(0, 10000))
#random_seed = 7900
random_seed = helper.get_seed(random_seed)
helper.set_seed(random_seed)

# Get time
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# Parameters for draw speed
frame_rate = 1

##########################################################################
# Knobs to turn
##########################################################################

# Canvas size
w = 1000  # width
h = 1000  # height


##########################################################################
# setup()
# function gets run once at start of program
##########################################################################

def setup():

    # Sets size of canvas in pixels (must be first line)
    size(w, h)

    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high

    # Sets color space to Hue Saturation Brightness with max values of HSB
    # respectively
    colorMode(HSB, 360, 100, 100, 100)

    # Set the number of frames per second to display
    frameRate(frame_rate)

    background(0, 0, 95)

    rectMode(CORNER)

    # Stops draw() from running in an infinite loop (should be last line)
    #noLoop()  # Comment to run draw() infinitely (or until 'count' hits limit)


##########################################################################
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
##########################################################################

def draw():
    step = 20
    # if frameCount == step*2:
    #     exit()

    counter = frameCount % 100

    background(g.backgroundColor)

    noFill()
    stroke(0, 0, 25)

    r = 200

    translate(width / 2, height / 2)

    # Full bug
    w_bug = random(300, 600)
    # Calculate based on ratio (w_bug*random_multiplier)
    h_bug = random(500, 800)
    x_0 = 0 - w_bug / 2
    y_0 = 0 - h_bug / 2

    # Head
    w_head_offset = 0.5
    x_head = x_0+w_bug*(1-w_head_offset)/2
    y_head = y_0
    w_head = w_bug*w_head_offset
    h_head = random(h_bug * 0.1, h_bug * 0.2)

    # Pronotum
    w_pron_offset = 0.9
    g_pron = random(0, 15)  # gap
    x_pron = x_0+w_bug*(1-w_pron_offset)/2
    y_pron = y_head + h_head + g_pron
    w_pron = w_bug*w_pron_offset
    h_pron = random(0, h_bug * 0.3)

    # Elytron
    g_elyt = random(0, 15)
    x_elyt = x_0
    y_elyt = y_pron + h_pron + g_elyt
    w_elyt = w_bug
    h_elyt = h_bug - h_head - h_pron

    w_eyes = 50
    h_eyes = 50
    

    
    fill(0, 0, 50)
    head = get_16_points(x_head, y_head, w_head, h_head)
    pron = get_16_points(x_pron, y_pron, w_pron, h_pron)
    elyt = get_16_points(x_elyt, y_elyt, w_elyt, h_elyt)
    l_wing = get_16_points(elyt[0][0], elyt[0][1], w_elyt / 2, h_elyt)
    r_wing = get_16_points(elyt[2][0], elyt[2][1], w_elyt / 2, h_elyt)
    l_eye = get_16_points(head[1][0]-w_eyes/2, head[1][1], h_eyes, w_eyes)
    r_eye = get_16_points(head[3][0]-w_eyes/2, head[3][1], h_eyes, w_eyes)

    
    ##########################################################################
    # Antennae
    ##########################################################################
    
    # beginShape()
    # cvp(*head[2])
    # cvp(*head[7]) if pointed else cvp(*head[6])
    # cvp(*head[10])
    # cvp(*head[13]) if pointed else cvp(*head[14])
    # cvp(*head[2])
    # cvp(*head[7]) if pointed else cvp(*head[6])
    # cvp(*head[10])
    # endShape() 
    
    ##########################################################################
    # Neck
    ##########################################################################
    pushStyle()
    curveTightness(0.9)
    
    m = createGraphics(width, height)
    m.beginDraw()
    m.pushMatrix()
    m.translate(width/2, height/2)
    m.beginShape()
    m.curveTightness(0.9)
    m.curveVertex(head[12][0]+w_head*0.05, head[11][1]-g_pron*2)
    m.curveVertex(head[8][0]-w_head*0.05, head[9][1]-g_pron*2)
    m.curveVertex(head[8][0]+w_head*0.2, head[9][1]+g_pron*2)
    m.curveVertex(head[12][0]-w_head*0.2, head[11][1]+g_pron*2)
    m.curveVertex(head[12][0]+w_head*0.05, head[11][1]-g_pron*2)
    m.curveVertex(head[8][0]-w_head*0.05, head[9][1]-g_pron*2)
    m.curveVertex(head[8][0]+w_head*0.2, head[9][1]+g_pron*2)
    m.endShape()
    m.endDraw()
    m.popMatrix()
    
    pattern = get_pattern('dots', 0.3)
    pattern.mask(m)
    image(pattern, -width/2, -height/2)
    
    pushStyle()
    noFill()
    stroke(0, 0, 20)
    beginShape()
    cvp(head[12][0]+w_head*0.1, head[11][1]-g_pron)
    cvp(head[8][0]-w_head*0.1, head[9][1]-g_pron)
    cvp(head[8][0]+w_head*0.2, head[9][1]+g_pron*2)
    cvp(head[12][0]-w_head*0.2, head[11][1]+g_pron*2)
    cvp(head[12][0]+w_head*0.1, head[11][1]-g_pron)
    cvp(head[8][0]-w_head*0.1, head[9][1]-g_pron)
    cvp(head[8][0]+w_head*0.2, head[9][1]+g_pron*2)
    endShape()
    popStyle()
    
    ##########################################################################
    # Eyes
    ##########################################################################
    l_eye[8][0] -= 10
    l_eye[8][1] -= 10
    r_eye[12][0] += 10
    r_eye[12][1] -= 10
    
    pushStyle()
    fill(0, 0, 90)
    curveTightness(-0.5)
    beginShape()
    cvp(*l_eye[15])
    cvp(*l_eye[4])
    cvp(*l_eye[8])
    cvp(*l_eye[13])
    cvp(*l_eye[15])
    cvp(*l_eye[4])
    cvp(*l_eye[8])
    endShape()
    
    beginShape()
    cvp(*r_eye[0])
    cvp(*r_eye[5])
    cvp(*r_eye[7])
    cvp(*r_eye[12])
    cvp(*r_eye[0])
    cvp(*r_eye[5])
    cvp(*r_eye[7])
    endShape()
    
    popStyle()
    curveTightness(0)


    ##########################################################################
    # Head
    ##########################################################################
    # Pokey head or a round head
    pointed = True
    
    m = createGraphics(width, height)
    m.beginDraw()
    m.pushMatrix()
    m.translate(width/2, height/2)
    m.beginShape()
    m.curveVertex(*head[2])
    m.curveVertex(*head[7]) if pointed else m.curveVertex(*head[6])
    m.curveVertex(*head[10])
    m.curveVertex(*head[13]) if pointed else m.curveVertex(*head[14])
    m.curveVertex(*head[2])
    m.curveVertex(*head[7]) if pointed else m.curveVertex(*head[6])
    m.curveVertex(*head[10])
    m.endShape()
    m.endDraw()
    m.popMatrix()
    
    pattern = get_pattern('dots', 0.5)
    pattern.mask(m)
    image(pattern, -width/2, -height/2)
    
    pushStyle()
    noFill()
    stroke(0, 0, 20)
    beginShape()
    cvp(*head[2])
    cvp(*head[7]) if pointed else cvp(*head[6])
    cvp(*head[10])
    cvp(*head[13]) if pointed else cvp(*head[14])
    cvp(*head[2])
    cvp(*head[7]) if pointed else cvp(*head[6])
    cvp(*head[10])
    endShape()
    popStyle()
    
    
    ##########################################################################
    # Legs
    ##########################################################################
    wing_x_squeeze = 50
    
    elyt[7][0] -= wing_x_squeeze*1.1
    elyt[13][0] += wing_x_squeeze*1.1
    elyt[14][0] += wing_x_squeeze
    
    elyt[0] = [pron[12][0], pron[12][1]-h_pron*0.1]
    elyt[2] = [pron[10][0], pron[10][1]-h_pron*0.1]
    elyt[4] = [pron[8][0], pron[8][1]-h_pron*0.1]
    
    arm_length_a = w_elyt*random(0.01, 0.1)
    arm_length_b = h_elyt*random(0.2, 0.4)
    arm_length_c = h_elyt*random(0.2, 0.5)
    arm_length_d = 50
    arm_width_a = 20
    arm_width_b = 20
    arm_width_c = 20
    arm_width_d = 20
    
    up_angle_a = random(200, 260)
    up_angle_b = random(210, 270)
    up_angle_c = random(215, 270)
    dn_angle_a = random(145, 185)
    dn_angle_b = random(85, 125)
    dn_angle_c = random(75, 115)
    
    
    
    draw_leg(pron[14][0], pron[14][1], arm_length_a, up_angle_a, 50, arm_length_b, up_angle_b, 5, arm_length_c, up_angle_c, 5)
    draw_leg(elyt[15][0], elyt[15][1], arm_length_a, dn_angle_a, 50, arm_length_b, dn_angle_b, 5, arm_length_c, dn_angle_c, 5, True)
    draw_leg(elyt[14][0], elyt[14][1], arm_length_a, dn_angle_a, 50, arm_length_b, dn_angle_b, 5, arm_length_c, dn_angle_c, 5, True)
    pushMatrix()
    scale(-1.0, 1.0)  
    draw_leg(pron[14][0], pron[14][1], arm_length_a, up_angle_a, 50, arm_length_b, up_angle_b, 5, arm_length_c, up_angle_c, 5)
    draw_leg(elyt[15][0], elyt[15][1], arm_length_a, dn_angle_a, 50, arm_length_b, dn_angle_b, 5, arm_length_c, dn_angle_c, 5, True)
    draw_leg(elyt[14][0], elyt[14][1], arm_length_a, dn_angle_a, 50, arm_length_b, dn_angle_b, 5, arm_length_c, dn_angle_c, 5, True)
    popMatrix()
    
    
    ##########################################################################
    # Elytron
    ##########################################################################
    m = createGraphics(width, height)
    m.beginDraw()
    m.pushMatrix()
    m.translate(width/2, height/2)
    m.beginShape()
    m.curveVertex(*elyt[0])
    m.curveVertex(*elyt[2])
    m.curveVertex(*elyt[4])
    m.curveVertex(*elyt[7])
    m.curveVertex(*elyt[10])
    m.curveVertex(*elyt[13])
    m.curveVertex(*elyt[0])
    m.curveVertex(*elyt[2])
    m.curveVertex(*elyt[4])
    m.endShape()
    m.endDraw()
    m.popMatrix()

    pattern = get_pattern('dots', 0.3)
    pattern.mask(m)
    image(pattern, -width/2, -height/2)
    

    pushStyle()
    noFill()
    stroke(0, 0, 20)
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
    popStyle()

    ##########################################################################
    # Pronotum
    ##########################################################################
    pron[0][0] += w_pron*0.1
    pron[4][0] -= w_pron*0.1

        
    m = createGraphics(width, height)
    m.beginDraw()
    m.pushMatrix()
    m.translate(width/2, height/2)
    m.beginShape()
    m.curveVertex(*pron[0])
    m.curveTightness(0.7)
    m.curveVertex(*pron[2])
    m.curveTightness(0)
    m.curveVertex(*pron[4])
    m.curveVertex(*pron[7])
    m.curveTightness(0.7)
    m.curveVertex(*pron[10])
    m.curveTightness(0)
    m.curveVertex(*pron[13])
    m.curveVertex(*pron[0])
    m.curveTightness(0.7)
    m.curveVertex(*pron[2])
    m.curveTightness(0)
    m.curveVertex(*pron[4])
    m.endShape()
    m.endDraw()
    m.popMatrix()

    pattern = get_pattern('dots', 0.5)
    pattern.mask(m)
    image(pattern, -width/2, -height/2)
    
    # Outline
    pushStyle()
    noFill()
    stroke(0, 0, 20)
    beginShape()
    cvp(*pron[0])
    curveTightness(0.7)
    cvp(*pron[2])
    curveTightness(0)
    cvp(*pron[4])
    cvp(*pron[7])
    curveTightness(0.7)
    cvp(*pron[10])
    curveTightness(0)
    cvp(*pron[13])
    cvp(*pron[0])
    curveTightness(0.7)
    cvp(*pron[2])
    curveTightness(0)
    cvp(*pron[4])
    endShape()
    popStyle()
    
    ##########################################################################
    # Wing Coverings
    ##########################################################################
    wing_mid_offset = 50
    #elyt[2][1] += 50

    r_wing[7][0] -= wing_x_squeeze
    l_wing[13][0] += wing_x_squeeze



#     # Right wing
#     pushMatrix()
#     # rotate(-PI/40)
#     beginShape()
#     cvp(*r_wing[15])
#     curveTightness(0.9)
#     cvp(*r_wing[1])
#     curveTightness(0)
#     cvp(*r_wing[4])
#     cvp(*r_wing[7])
#     cvp(*r_wing[12])
#     cvp(*r_wing[15])
#     curveTightness(0.9)
#     cvp(*r_wing[1])
#     curveTightness(0)
#     cvp(*r_wing[4])
#     endShape()
#     popMatrix()
    
    pattern = get_pattern('dots')
        
    # Left wing (to be mirrored)
    m = createGraphics(width, height)
    m.beginDraw()
    m.pushMatrix()
    # rotate(PI/40)
    m.translate(width/2, height/2)
    m.beginShape()
    m.curveVertex(*l_wing[0])
    m.curveVertex(*l_wing[2])
    m.curveVertex(l_wing[5][0], l_wing[5][1]-h*0.05)
    m.curveVertex(*l_wing[8])
    m.curveTightness(0.9)
    m.curveVertex(*l_wing[13])
    m.curveTightness(0)
    m.curveVertex(*l_wing[0])
    m.curveVertex(*l_wing[2])
    m.curveVertex(l_wing[5][0], l_wing[5][1]-h*0.05)
    m.endShape()
    m.endDraw()
    m.popMatrix()
    
    # Clip/Mask the pattern to wing size
    pattern.mask(m)
    pushMatrix()
    image(pattern, -width/2, -height/2)
    outline_wing(l_wing)
    # Mirror the wing
    scale(-1.0, 1.0)
    image(pattern, -width/2, -height/2)
    outline_wing(l_wing)
    popMatrix()




    helper.save_frame_timestamp('buggies', timestamp, random_seed)

    # Save memory by closing image, just look at it in the file system
    # if (w > 1000) or (h > 1000):
    #     exit()


##########################################################################
# Functions
##########################################################################

def draw_leg(x, y, length_a=100, angle_a=165, span_a=50, length_b=200, angle_b=105, span_b=5, length_c=200, angle_c=95, span_c=5, upper_leg=False):
    # Arm A
    angle = angle_a
    span = span_a
    x = x+5
    y = y
    ax1, ay1 = helper.circle_points(x+20, y, -10, radians(angle+span+180))
    ax2, ay2 = helper.circle_points(x+20, y, -10, radians(angle+180))
    ax3, ay3 = helper.circle_points(x+20, y, -10, radians(angle-span+180))
    ax4, ay4 = helper.circle_points(x, y, length_a, radians(angle-span))
    ax5, ay5 = helper.circle_points(x, y, length_a, radians(angle))
    ax6, ay6 = helper.circle_points(x, y, length_a, radians(angle+span))
    
    # Arm B
    angle = angle_b
    span = span_b
    x = ax4
    y = ay4
    bx1, by1 = helper.circle_points(x-span, y, 0, radians(angle+span+180))
    bx2, by2 = helper.circle_points(x, y, 0, radians(angle+180))
    bx3, by3 = helper.circle_points(x+span, y, 0, radians(angle-span+180))
    bx4, by4 = helper.circle_points(x, y, length_b, radians(angle-span))
    bx5, by5 = helper.circle_points(x, y, length_b, radians(angle))
    bx6, by6 = helper.circle_points(x, y, length_b, radians(angle+span))
    
    # Arm C
    angle = angle_c
    span = span_c
    x = bx5
    y = by5
    cx1, cy1 = helper.circle_points(x-span, y, 0, radians(angle+span+180))
    cx2, cy2 = helper.circle_points(x, y, 0, radians(angle+180))
    cx3, cy3 = helper.circle_points(x+span, y, 0, radians(angle-span+180))
    cx4, cy4 = helper.circle_points(x, y, length_c, radians(angle-span))
    cx5, cy5 = helper.circle_points(x, y, length_c, radians(angle))
    cx6, cy6 = helper.circle_points(x, y, length_c, radians(angle+span))
    
    beginShape()
    cvp(cx1, cy1) if upper_leg else  cvp(cx3, cy3)
    cvp(cx2, cy2)
    cvp(cx3, cy3) if upper_leg else  cvp(cx1, cy1)
    cvp(cx4, cy4)
    cvp(cx5, cy5)
    cvp(cx6, cy6)
    cvp(cx1, cy1) if upper_leg else  cvp(cx3, cy3)
    cvp(cx2, cy2)
    cvp(cx3, cy3) if upper_leg else  cvp(cx1, cy1)
    endShape()
    
    beginShape()
    cvp(bx1, by1) if upper_leg else  cvp(bx3, by3)
    cvp(bx2, by2)
    cvp(bx3, by3) if upper_leg else  cvp(bx1, by1)
    cvp(bx4, by4)
    cvp(bx5, by5)
    cvp(bx6, by6)
    cvp(bx1, by1) if upper_leg else  cvp(bx3, by3)
    cvp(bx2, by2)
    cvp(bx3, by3) if upper_leg else  cvp(bx1, by1)
    endShape()
    
    beginShape()
    cvp(ax1, ay1)
    cvp(ax2, ay2)
    cvp(ax3, ay3)
    cvp(ax4, ay4)
    cvp(ax5, ay5)
    cvp(ax6, ay6)
    cvp(ax1, ay1)
    cvp(ax2, ay2)
    cvp(ax3, ay3)
    endShape()


def get_pattern(pattern_style, lightness_offset=1):

    if pattern_style == 'dots':
        pattern = createGraphics(width, height)
        pattern.beginDraw()
        pattern.pushMatrix()
        pattern.background(color(0, 13, 74*lightness_offset)) # mauve
        #pattern.translate(width/2, height/2)
        pattern.noStroke()
        pattern.fill(color(150, 22, 56*lightness_offset)) # green
        for i in range(40):
            r = random(5, 80)
            x = random(0, width)
            y = random(0, height)
            print(x, y, r)
            pattern.ellipse(x, y, r, r*random(1.2, 3))
        pattern.endDraw()
        pattern.popMatrix
        
    elif pattern_style == 'gradient':
        pattern = createGraphics(width, height)
        pattern.beginDraw()
        pattern.pushMatrix()
        pattern.background(color(0, 100, 100*lightness_offset)) # mauve
        #pattern.translate(width/2, height/2)
        pattern.noStroke()
        for i in range(40):
            pattern.fill(color(random(0, 360), random(20,30), random(60,90), 50*lightness_offset)) # green
            r = random(200, 1000)
            x = random(0, width)
            y = random(0, height)
            print(x, y, r)
            pattern.ellipse(x, y, r, r)
        pattern.endDraw()
        pattern.popMatrix
        
    return pattern


def outline_wing(l_wing):
    pushStyle()
    noFill()
    stroke(0, 0, 20)
    
    pushMatrix()
    # rotate(PI/40)
    beginShape()
    cvp(*l_wing[0])
    cvp(*l_wing[2])
    cvp(l_wing[5][0], l_wing[5][1]-h*0.05)
    cvp(*l_wing[8])
    curveTightness(0.9)
    cvp(*l_wing[13])
    curveTightness(0)
    cvp(*l_wing[0])
    cvp(*l_wing[2])
    cvp(l_wing[5][0], l_wing[5][1]-h*0.05)
    endShape()
    popMatrix()
    popStyle()
    

def cvp(x, y):
    curveVertex(x, y)
    #ellipse(x, y, 5, 5)


def get_16_points(x, y, w, h):
    points = [0] * 16
    points[0] = [x, y]
    points[1] = [x + w * 0.25, y]
    points[2] = [x + w * 0.5, y]
    points[3] = [x + w * 0.75, y]
    points[4] = [x + w, y]
    points[5] = [x + w, y + h * 0.25]
    points[6] = [x + w, y + h * 0.5]
    points[7] = [x + w, y + h * 0.75]
    points[8] = [x + w, y + h]
    points[9] = [x + w * 0.75, y + h]
    points[10] = [x + w * 0.5, y + h]
    points[11] = [x + w * 0.25, y + h]
    points[12] = [x, y + h]
    points[13] = [x, y + h * 0.75]
    points[14] = [x, y + h * 0.5]
    points[15] = [x, y + h * 0.25]
    return points


def draw_16_points(points):
    beginShape()
    for p in points + points[0:3]:
        cvp(*p)
    endShape()


def draw_12_points(points):
    #points = [points[i] for i in [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15]]
    curveTightness(0.3)
    beginShape()
    for p in points + points[0:3]:
        cvp(*p)
    endShape()

def mousePressed():
    helper.save_frame_timestamp('buggies', timestamp, random_seed)
