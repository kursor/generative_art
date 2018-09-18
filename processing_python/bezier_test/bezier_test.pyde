################################################################################
# Aaron Penne 
# 2018-09-16
# https://github.com/aaronpenne
################################################################################

import datetime
import string
import math
import sys
from random import shuffle, seed

# Define globals here
rand_seed = 1138

#seed(rand_seed)

frame_rate = 10
w = 1000  # width
h = 1000  # height
count = 0
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
anchors = []
len_anchors = 0
offset = []
len_offset = 0


pal = [(60, 7, 86),   #dcdccc cream
       (0, 28, 80),   #cc9393 pink
       (180, 9, 69),  #9fafaf blue gray
       (0, 13, 74),   #bca3a3 mauve
       (24, 31, 100), #ffcfaf peach
       (150, 22, 56), #709080 green
       (0, 0, 100),
      ]

def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)
        
    # Set the number of frames per second to display
    frameRate(frame_rate)
    
    imageMode(CENTER)
    rectMode(CENTER)
    ellipseMode(CENTER)
    
    global anchors, len_anchors
    anchors = range_float(0-PI/2, TWO_PI-PI/2, TWO_PI/5)
    len_anchors = len(anchors)
    
    global offset, len_offset
    offset = [5, -5, 20, -20, 50, -50]
    len_offset = len(offset)
    
    # Stops draw() from running in an infinite loop (should be last line)
    #randomSeed(rand_seed)
    #noLoop()


def draw():
    global count
    print(count)
    if count >= len_offset-1:
        sys.exit(0)
    count += 1
    
    off = offset[count]

    background(0, 0, 90)
    
    strokeWeight(3)
    stroke(0, 0, 0)
    
    beginShape()
    curveVertex(10*w/30, h*0.9)
    curveVertex(10*w/30, h*0.9)

    curveVertex(off + 2.5*w/6, h*0.5)
    
    curveVertex((-off *0.2)+3*w/6, h*0.1)

    curveVertex(off + 3.5*w/6, h*0.5)
    
    curveVertex(20*w/30, h*0.9)
    curveVertex(20*w/30, h*0.9)
    vertex(10*w/30, h*0.9)
    endShape()

            
    save_frame_timestamp('bezier_test', timestamp)

                   
def save_frame_timestamp(filename, timestamp='', output_dir='output'):
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_####.png'.format(timestamp, filename))
    saveFrame(output_filename)
    print(output_filename)
    
    
def save_timestamp(filename, timestamp='', output_dir='output'):
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_####.png'.format(timestamp, filename))
    save(output_filename)
    print(output_filename)
    
def random_list_value(val_list):
    index = int(random(0, len(val_list)))
    value = val_list[index]
    return value
        
        
def random_centered(value_og, offset=5):
    value = random(value_og-offset, value_og+offset)
    return value

def random_gaussian_limit(min_val, max_val):
    new_val = max_val*randomGaussian()+min_val
    if new_val < min_val:
        new_val = min_val
    elif new_val > max_val:
        new_val = max_val
    return new_val


def circle_points(origin_x, origin_y, r=50, a=0):
    x = origin_x + (r * cos(a))
    y = origin_y + (r * sin(a))
    return x, y


def range_float(start_val, end_val, inc_val):
    start_val = float(start_val)
    end_val = float(end_val)
    inc_val = float(inc_val)

    count = int(math.ceil((end_val - start_val) / inc_val))

    L = [None,] * count

    L[0] = start_val
    for i in xrange(1,count):
        L[i] = L[i-1] + inc_val
    return L
