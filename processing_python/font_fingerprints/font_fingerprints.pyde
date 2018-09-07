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
w = 2000  # width
h = 2500  # height
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
        
    # Stops draw() from running in an infinite loop (should be last line)
    randomSeed(rand_seed)
    noLoop()


def draw():
    global count
    if count > 5000:
        sys.exit(0)
    count += 1

    # Read font list
    try:
        with open('font_list_mac.txt', 'r') as f:
            font_list = f.read().splitlines()
    except:
        print('Using all fonts')
        font_list = PFont.list()
    
    #font_list = ['Amarillo']
    
    # filter_list = ['Bold', 'Italic', 'Heavy', 'Black', 'Light']
    # font_list_text = [x for x in PFont.list() if ~any(f in x for f in filter_list)]
    # # Get the fonts in a text file
    # with open('font_list_mac.txt', 'w+') as f:
    #     for font in font_list_text:
    #         f.write('{}\n'.format(font)) 
    
    text_size = 300
    
    for font in font_list:
        
        # Background color
        # hue_val = random_centered(26.7, 5)
        # sat_val = random_centered(3.7, 3)
        # bri_val = random_centered(95.3, 3)
        background(26.7, 3.7, 95.3) #f3eeea
        
        # Initialize font
        text_font = createFont(font, text_size)
        textFont(text_font)
        
        # Text properties
        fill(0, 0, 4, 7)  #3f3f3f
        #fill(168, 31.7, 74.1, 4)  #81bdb1
        stroke(0, 0, 0)
        textAlign(CENTER, BOTTOM)
        textSize(text_size)
        
        # Print each string at different locations
        offset = h/6
        offset_pad = h*0.045
        
        print_string_stack(string.punctuation, 1*offset+offset_pad)
        
        print_string_stack(string.ascii_lowercase, 2*offset+offset_pad)
        
        full_string = string.ascii_lowercase + string.ascii_uppercase + string.digits
        print_string_stack(full_string, 3*offset+offset_pad)
        
        print_string_stack(string.ascii_uppercase, 4*offset+offset_pad)
        
        print_string_stack(string.digits, 5*offset+offset_pad)
            
        # Prints the name of the font
        text_font = createFont('LucidaSans-Typewriter', text_size)
        textFont(text_font)
        fill(0, 0, 0, 30)
        textAlign(CENTER, BOTTOM)
        textSize(35)
        text(font, w/2, 5.6*offset)
        
        
        font_name = font.replace('\\', '')
        font_name = font.replace('/', '')
        output_filename = os.path.join('output', '{}_{}.png'.format(timestamp, font_name))
        saveFrame(output_filename)
        print(output_filename)
    
def random_list_value(val_list):
    index = int(random(0, len(val_list)))
    value = val_list[index]
    return value
        
        
def random_centered(value_og, offset=5):
    value = random(value_og-offset, value_og+offset)
    return value

    
def print_string_stack(string_stack='TESt', offset=100):
    for c in string_stack:
        text(c, w/2, offset)
     
     
def create_filename(word, num_list=[]):
    filename = word
    for number in num_list:
        filename = filename + '_{:04}'.format(int(number))
    filename = filename + '.png'
    return filename
