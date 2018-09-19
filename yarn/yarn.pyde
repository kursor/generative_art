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

################################################################################
# Global variables
################################################################################

# Get time 
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# Set random seed value for both Python 'random' and Processing 'random'
rand_seed = 1138
# Comment out seeds below to get new shape on every run
#seed(rand_seed) # This only applys to the Python random functions
#randomSeed(rand_seed) # This only applys to the Processing random functions

# Parameters for canvas and draw speed
frame_rate = 10
w = 1000  # width
h = 1000  # height

# Parameters for points around circle
num_anchors = 50
# These globals are populated in setup()
anchors = []
len_anchors = 0

# Zenburn color palette
pal = [(60, 7, 86),   #dcdccc cream
       (0, 28, 80),   #cc9393 pink
       (180, 9, 69),  #9fafaf blue gray
       (0, 13, 74),   #bca3a3 mauve
       (24, 31, 100), #ffcfaf peach
       (150, 22, 56), #709080 green
       (0, 0, 100),
      ]

# Counter to allow for tracking draw() runs
count = 0

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
    
    # Determine anchor points around circle for the curves to hit
    global anchors, len_anchors
    anchors = range_float(0-PI/2, TWO_PI-PI/2, TWO_PI/num_anchors)
    len_anchors = len(anchors)

    # Stops draw() from running in an infinite loop (should be last line)
    noLoop()  # Comment to run draw() infinitely (or until 'count' hits limit) 


################################################################################
# draw() 
# function gets run repeatedly (unless noLoop() called in setup())
################################################################################

def draw():
    # Loop counter to control number of draw() runs
    global count
    print(count)
    if count >= len_anchors-1:
        sys.exit(0)
    count += 1

    # Parameters for run (knobs to turn)
    radius = 300
    
    # Aesthetics of lines
    strokeWeight(3)
    stroke(0, 0, 0)
    noFill()

    background(0, 0, 90)

    # Moves origin to center of image so (0,0) becomes center instead of (w/2,h/2)
    translate(w/2, h/2)
        
    ################################################################################
    # Actual shape drawing begins
    ################################################################################
    
    # Get three start/end points. The curve needs to retrace these 3 points to connect in a smooth loop 
    # https://forum.processing.org/two/discussion/14849/how-to-form-a-smooth-loop-using-curve
    beginShape()
    x_0, y_0 = circle_points(0, 0, radius, random_list_value(anchors))
    curveVertex(x_0, y_0)
    x_1, y_1 = circle_points(0, 0, radius, random_list_value(anchors))
    curveVertex(x_1, y_1)
    x_2, y_2 = circle_points(0, 0, radius, random_list_value(anchors))
    curveVertex(x_2, y_2)

    # Shuffle the list to allow for randomized points around the circle
    shuffle(anchors)
    
    # Loop through list of anchor points and draw curves between them (best if shuffled first)
    for a in anchors:
        # radius = random_centered(radius, 30) # Randomize the radius a bit for each point
        x, y = circle_points(0, 0, radius, a)
        curveVertex(x, y)
        
        # Loop through all the points again for a weird effect
        # for a in anchors:
        #     # radius = random_centered(radius, 30) # Randomize the radius a bit for each point
        #     x, y = circle_points(0, 0, radius, a)
        #     curveVertex(x, y)

    # Run the curve through the starting three points to ensure smooth connection at the end
    curveVertex(x_0, y_0)
    curveVertex(x_1, y_1)
    curveVertex(x_2, y_2)
    endShape()
    
    save_frame_timestamp('bezier_test', timestamp)


################################################################################
# Functions
################################################################################

def save_frame_timestamp(filename, timestamp='', output_dir='output'):
    '''Saves each frame with a structured filename to allow for tracking all output'''
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_####.png'.format(timestamp, filename))
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
