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
    size(w, h, P3D) # (width, height)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)
        
    # Set the number of frames per second to display
    frameRate(frame_rate)
    
    imageMode(CENTER)
        
    # Stops draw() from running in an infinite loop (should be last line)
    #randomSeed(rand_seed)
    #noLoop()


def draw():
    global count
    if count > 30:
        sys.exit(0)
    count += 1
    
    background(0, 0, 100)
    translate(w/2, h/2)
    
    r = 20
    grid_x = [x for x in range(-300, 300, int(r*1.2))]
    grid_y = [y for y in range(-300, 300, int(r*1.2))]
    print(grid_x)
    
    # x_skip = int(random(0, len(grid_x)+1))
    # y_skip = int(random(0, len(grid_y)+1))
    # print(x_skip, y_skip)
    
    # Draw all the shadows first
    for ix, x in enumerate(grid_x):
        for iy, y in enumerate(grid_y):
            ellipse_values = (x, y, r*0.7, r*0.7)
            pushMatrix()
            translate(0, 0, -10)
            # if (ix!=x_skip) or (iy!=y_skip):
            #     shadow_ellipse(ellipse_values, colors_tuple=(0, 0, 0, 40), w_offset=0, h_offset=0, blur=7)
            shadow_ellipse(ellipse_values, colors_tuple=(0, 0, 0, 40), w_offset=0, h_offset=0, blur=5)
            popMatrix()
            
    # Draw all the circles next
    for ix, x in enumerate(grid_x):
        for iy, y in enumerate(grid_y):
            ellipse_values = (x, y, r, r)
            noStroke()
            fill(0,0,100)
            pushMatrix()
            z = random(-10, 5)
            translate(0, 0, z)
            print(ix, iy, z)
            # if (ix!=x_skip) or (iy!=y_skip):
            #     ellipse(*ellipse_values)
            ellipse(*ellipse_values)
            popMatrix()
        
    save_frame_timestamp('ellipse', timestamp)


def shadow_ellipse(values_tuple, colors_tuple=(0, 0, 0, 80), w_offset=10, h_offset=20, blur=10):
    x_shape = values_tuple[0]
    y_shape = values_tuple[1]
    w_shape = values_tuple[2]
    h_shape = values_tuple[3]
    
    shadow = createGraphics(int(w_shape*4), int(h_shape*4))
    shadow.beginDraw()
    shadow.noStroke()
    shadow.fill(*colors_tuple)
    shadow.translate(w_shape*4/2, h_shape*4/2)
    shadow.ellipse(0+w_offset, 0+h_offset, w_shape, h_shape)
    shadow.endDraw()
    shadow.filter(BLUR, blur)
    image(shadow, x_shape, y_shape)
    
                   
                   
def save_frame_timestamp(filename, timestamp='', output_dir='output'):
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_###.png'.format(timestamp, filename))
    saveFrame(output_filename)
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
                                    
                          
def print_string_stack(string_stack='TESt', w_offset=100, h_offset=100):
    for c in string_stack:
        text(c, w_offset, h_offset)
     
     
def create_filename(word, num_list=[]):
    filename = word
    for number in num_list:
        filename = filename + '_{:04}'.format(int(number))
    filename = filename + '.png'
    return filename
