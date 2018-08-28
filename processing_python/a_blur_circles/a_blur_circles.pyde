################################################################################
# Aaron Penne 
# 2018-08-28
# https://github.com/aaronpenne
################################################################################

import math

# Define globals here
rand_seed = 1138
frame_rate = 1
w = 800  # width
h = 800  # height
border_pad = 60



def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)
        
    # Set the number of frames per second to display
    frameRate(frame_rate)
        
    # Set the psuedorandom seed
    randomSeed(rand_seed)
    
    # Set (x, y) for circles to center
    ellipseMode(CENTER)
    
    background(0, 0, 97)
    
    # Stops draw() from running in an infinite loop (should be last line)
    noLoop()



def draw():

    # noFill()
    # ellipse(w/2, h/2, 160, 160)
    # ellipse(w/2, h/2, 240, 240)


    # Dot circles (looks like spraypaint)
    # for spread in [5, 7, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20]:
    #     circle_dots(hsba=(0, 0, 0, 5), num_dots=100000, spread=spread, stroke_weight=0.7)
        
    circle_lines(hsba=(0, 0, 0, 5), center=(w/2,h/2), num_lines=1000, radius=(150, 150), spread=20, stroke_weight=0.5)
    circle_lines(hsba=(0, 0, 0, 5), center=(w/2,h/2), num_lines=3000, radius=(400, 400), spread=50, stroke_weight=0.5)
    
    # Dot circles (looks like spraypaint)
    spread = [5, 7, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20]
    circle_dots(hsba=(0, 0, 0, 5), num_dots=100000, radius=(150, 150), spread=spread, stroke_weight=0.7)
    circle_dots(hsba=(0, 0, 0, 5), num_dots=100000, radius=(300, 300), spread=spread, stroke_weight=0.7)
     
    
    #border()
    filename = create_filename('test')
    saveFrame('output/blur_circles_######.png')
    #print('concentric_{:02}_{:02}_{:01}.png'.format(num_circles, num_cols, int(xy_noise*10)))

def circle_dots(hsba=(0, 50, 50, 50), center=(w/2,h/2), num_dots=100, radius=(200,200), spread=[10], stroke_weight=5):
    for s in spread:
        for i in range(num_dots):
            r_offset = randomGaussian()*s
            x = center[0] + (radius[0] + r_offset) * cos(TWO_PI * i / num_dots) 
            y = center[1] + (radius[1] + r_offset) * sin(TWO_PI * i / num_dots)
            strokeWeight(stroke_weight)
            stroke(color(*hsba))
            point(x, y)
        
def circle_lines(hsba=(0, 50, 50, 50), center=(w/2,h/2), num_lines=100, radius=(200, 200), spread=10, stroke_weight=1):
    for i in range(num_lines):
        r_offset = randomGaussian()*spread
        r_x = radius[0] + r_offset
        r_y = radius[1] + r_offset
        noFill()
        strokeWeight(stroke_weight)
        stroke(color(*hsba))
        ellipse(w/2, h/2, r_x, r_y)
    
def border():
    noStroke()
    fill(color(0, 0, 0))
    #fill(g.backgroundColor)
    rect(0, 0, width, border_pad)  # Top
    rect(0, 0, border_pad, height)  # Left
    rect(0, height - border_pad, width, border_pad)  # Bottom
    rect(width - border_pad, 0, border_pad, height)  # Right
    
def create_filename(word, num_list=[]):
    filename = word
    for number in num_list:
        filename = filename + '_{:04}'.format(int(number))
    filename = filename + '.png'
    return filename
    
def annotate(num_circles, num_cols, xy_noise):
    stroke(0)
    fill(0)
    textFont(createFont('Courier',100))
    textAlign(LEFT, TOP)
    textSize(height*0.013)
    text('concentric_{:02}_{:02}_{:01}.png\nEmulating @paulrickards'.format(num_circles, num_cols, int(xy_noise*10)), width*pad_pct, height - (height*pad_pct*0.9))
    textAlign(RIGHT, TOP)
    text('Aaron Penne', width - width*pad_pct, height - (height*pad_pct*0.9))
    
    



    
