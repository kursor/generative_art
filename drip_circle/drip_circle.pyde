################################################################################
# Aaron Penne
# https://github.com/aaronpenne
################################################################################

import datetime
import string
import math
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
frame_rate = 10

################################################################################
# Color palettes #FIXME need a library of these or something...
################################################################################

# Zenburn color palette
# pal = [(60, 7, 86),   #dcdccc cream
#        (0, 28, 80),   #cc9393 pink
#        (180, 9, 69),  #9fafaf blue gray
#        (0, 13, 74),   #bca3a3 mauve
#        (24, 31, 100), #ffcfaf peach
#        (150, 22, 56), #709080 green
#        #(0, 0, 100),
#       ]

# Warhol's Mick Jagger
# pal = [(41, 41, 66),  # brown
#        (342, 32, 85), # pink
#        #(45, 7, 96),   # cream
#        (354, 60, 72), # red
#        (98, 19, 87),  # green
#       ]

pal = [(348.7, 50.4, 94.9),  # bright salmon
       (306.6, 40.8, 96.1), # bright pink
       (45.7, 78.8, 94.1),  # yellow
       (16.3, 28.6, 96.1),  # salmon
       (358.7, 75.6, 94.9), # red
       ]

# Counter to allow for tracking draw() runs
count = 0


################################################################################
# Knobs to turn
################################################################################

# Canvas size
w = 500  # width
h = 500  # height

# Number of positions across canvas
radius = 26

num_steps = w/radius
locs_a = [x for x in range(0, num_steps+1, 2)]
locs_b = [x for x in range(1, num_steps+1, 2)]

offset_a = [random(0, 3*h/10) for x in locs_a]
offset_b = [random(0, 1.5*h/10) for x in locs_a]

color_line = 4*h/10

sin_steps = []
print(sin_steps)

################################################################################
# setup()
# function gets run once at start of program
################################################################################

def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)

    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high

    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)

    # Set the number of frames per second to display
    frameRate(frame_rate)

    rectMode(CORNERS)
    
    global sin_steps
    sin_steps = [1+sin(x) for x in range_float(0, TWO_PI+PI/20, PI/20)]
    sin_steps = sin_steps + sin_steps + sin_steps + sin_steps
    print(sin_steps)
    

    # Stops draw() from running in an infinite loop (should be last line)
    #noLoop()  # Comment to run draw() infinitely (or until 'count' hits limit)


################################################################################
# draw()
# function gets run repeatedly (unless noLoop() called in setup())
################################################################################

def draw():
    global count
    count += 1
    
    background(0, 0, 90)

    noStroke()

    fill(0, 0, 0)
    rect(0, 0, w, color_line)

    fill(0, 0, 100)
    rect(0, h, w, color_line)

    for loc, offset in zip(locs_a, offset_a):
        fill(0, 0, 0)
        #offset = abs(sin(loc))*100
        x = loc*radius
        y = color_line+offset+offset/4*sin_steps[count+loc]
        rect(x-radius/2, y, x+radius/2, 0)
        ellipse(x, y, radius, radius)
    for loc, offset in zip(locs_b, offset_b):
        fill(0, 0, 100)
        #offset = random(0, 1.5*h/10)
        x = loc*radius
        y = color_line-offset+offset/10*sin_steps[count+loc+10]
        rect(x-radius/2, y, x+radius/2, h)
        ellipse(x, y, radius, radius)

    save_frame_timestamp('drip_circle', timestamp)

    # Save memory by closing image, just look at it in the file system
    if (w > 1000) or (h > 1000):
        exit()


################################################################################
# Functions
################################################################################


def save_frame_timestamp(filename, timestamp='', output_dir='output'):
    '''Saves each frame with a structured filename to allow for tracking all output'''
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_{}_####.png'.format(timestamp, filename, random_seed))
    saveFrame(output_filename)
    print(output_filename)


def save_timestamp(filename, timestamp='', output_dir='output'):
    '''Saves image with a structured filename to allow for tracking all output'''
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_####.png'.format(timestamp, filename))
    save(output_filename)
    print(output_filename)


def random_list_value(val_list):
    '''Returns a random value from a list'''
    index = int(random(0, len(val_list)))
    value = val_list[index]
    return value


def random_centered(value_og, offset=5):
    '''Randomly varies value_og within the offset range'''
    value = random(value_og-offset, value_og+offset)
    return value


def random_gaussian_limit(min_val, max_val):
    '''Same as built-in randomGaussian but truncated to within a range'''
    new_val = max_val*randomGaussian()+min_val
    if new_val < min_val:
        new_val = min_val
    elif new_val > max_val:
        new_val = max_val
    return new_val


def circle_points(origin_x, origin_y, r=50, a=0):
    '''Returns cartesian coordinates given a circle origin, radius, and angle'''
    x = origin_x + (r * cos(a))
    y = origin_y + (r * sin(a))
    return x, y


def range_float(start_val, end_val, inc_val):
    '''
    Allows for similar functionality to built-in range() but with float step values
    Adapted from http://code.activestate.com/recipes/66472/
    '''
    start_val = float(start_val)
    end_val = float(end_val)
    inc_val = float(inc_val)

    count = int(math.ceil((end_val - start_val) / inc_val))

    L = [None,] * count

    L[0] = start_val
    for i in xrange(1,count):
        L[i] = L[i-1] + inc_val
    return L
