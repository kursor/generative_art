################################################################################
# Aaron Penne 
# 2018-08-28
# https://github.com/aaronpenne
################################################################################

import datetime
import string
import sys

# Define globals here
rand_seed = 1138
frame_rate = 1
w = 800  # width
h = 800  # height
count = 0
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

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
        
    # Stops draw() from running in an infinite loop (should be last line)
    randomSeed(rand_seed)
    noLoop()


def draw():
    global count
    if count > 1000:
        sys.exit(0)
    count += 1
    
    background(41.9, 34, 99.2)
    translate(w/2, h/2)
    noStroke()
    fill(0, 53.1, 88.6)
    
    grid_x = [-200, 0, 200]
    grid_y = [-200, 0, 200]
    #grid_x = [-600, -400, -200, 0, 200, 400, 600]
    #grid_y = [-600, -400, -200, 0, 200, 400, 600]
    
    for x in grid_x:
        for y in grid_y:
            ellipse_values = (x, y, 50, 50)
            shadow_ellipse(ellipse_values, colors_tuple=(0, 0, 0, 80), w_offset=10, h_offset=20, blur=0)
    for x in grid_x:
        for y in grid_y:
            ellipse_values = (x, y, 50, 50)
            fill(0, 53.1, 88.6)
            ellipse(*ellipse_values)
        


    save_frame_timestamp('ellipse', timestamp)


def shadow_ellipse(values_tuple, colors_tuple=(0, 0, 0, 80), w_offset=10, h_offset=20, blur=10):
    x_shape = values_tuple[0]
    y_shape = values_tuple[1]
    w_shape = values_tuple[2]
    h_shape = values_tuple[3]
    
    shadow = createGraphics(w_shape*4, h_shape*4)
    shadow.beginDraw()
    shadow.background(0, 0, 0)
    shadow.noStroke()
    shadow.fill(*colors_tuple)
    shadow.ellipse(0, 0, w_shape+x_offset, h_shape+y_offset)
    shadow.endDraw()
    shadow.filter(BLUR, blur)
    image(shadow, x_shape, y_shape)
    
                   
                   
def save_frame_timestamp(filename, timestamp='', output_dir='output'):
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}.png'.format(timestamp, filename))
    saveFrame(output_filename)
    print(output_filename)
    
    
def random_list_value(val_list):
    index = int(random(0, len(val_list)))
    value = val_list[index]
    return value
        
        
def random_centered(value_og, offset=5):
    value = random(value_og-offset, value_og+offset)
    return value

    
def print_string_stack(string_stack='TESt', w_offset=100, h_offset=100):
    for c in string_stack:
        text(c, w_offset, h_offset)
     
     
def create_filename(word, num_list=[]):
    filename = word
    for number in num_list:
        filename = filename + '_{:04}'.format(int(number))
    filename = filename + '.png'
    return filename
