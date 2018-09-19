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
w = 1000  # width
h = 1000  # height
count = 0
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')


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
        
    # Stops draw() from running in an infinite loop (should be last line)
    # randomSeed(rand_seed)
    noLoop()


def draw():
    global count
    if count > 30:
        sys.exit(0)
    count += 1
    
    background(0, 0, 25)
    
    translate(w/2, h/2)
    
    #create_mask()

    for offset in range(0, 41, 1):
        background(0, 0, 25)
        prev_c = pal[0]
        for ix, r in enumerate([100, 150, 200, 300, 400, 500, 600]):
            c = pal[ix]
            draw_shadow((prev_c[0], prev_c[1], 20, 70), (w/2+(offset-20)*ix, h/2+(offset-20)*ix, r, r), hard_offset=10+1000/r)
            draw_shape(c, (w/2+(offset-20)*ix, h/2+(offset-20)*ix, r+7, r+7))
            prev_c = c
            
        save_frame_timestamp('hole_{:02}'.format(offset), timestamp)

def draw_shadow(prev_color, next_shape_vals, hard_offset=10, soft_offset=-5):
    v = next_shape_vals
    img = createGraphics(w, h)
    img.beginDraw()
    img.colorMode(HSB, 360, 100, 100, 100)
    img.background(*prev_color)
    img.blendMode(REPLACE)
    img.fill(0, 0, 100, 0)
    img.noStroke()
    img.ellipse(v[0]+hard_offset, v[1]+hard_offset, v[2]-hard_offset, v[3]-hard_offset)
    img.blendMode(BLEND)
    img.endDraw()
    image(img, 0, 0)

    
def draw_shape(this_color, next_shape_vals):
    v = next_shape_vals
    img = createGraphics(w, h)
    img.beginDraw()
    img.colorMode(HSB, 360, 100, 100, 100)
    img.background(*this_color)
    img.blendMode(REPLACE)
    img.fill(0, 0, 100, 0)
    img.noStroke()
    img.ellipse(v[0], v[1], v[2], v[3])
    img.blendMode(BLEND)
    img.endDraw()
    image(img, 0, 0)
    

def create_mask():
    img = createGraphics(w, h)
    img.beginDraw()
    img.colorMode(HSB, 360, 100, 100, 100)
    img.fill(0, 0, 0)
    img.noStroke()
    img.ellipse(w/2, h/2, w*0.8, h*0.8)
    img.filter(BLUR, 20)
    img.endDraw()
    image(img, 0, 0)
        
                   
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
