################################################################################
# Aaron Penne 
# 2018-08-28
# https://github.com/aaronpenne
################################################################################

import math
import sys

# Define globals here
rand_seed = 1138
frame_rate = 1
w = 800  # width
h = 800  # height
border_pad = 60
count = 0



def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)
        
    # Set the number of frames per second to display
    frameRate(frame_rate)
    
    # Set (x, y) for circles to center
    ellipseMode(CENTER)
    
    background(0, 0, 97)
    
    # Stops draw() from running in an infinite loop (should be last line)
    randomSeed(rand_seed)
    noLoop()



def draw():

    background(0, 0, 97)
    
    # global count
    # print(count)
    # if count > 30:
    #     sys.exit(0)
    # count += 1

    # radius_list = [50, 100, 150, 200, 250, 300]
    # spread_list = [3, 5, 10, 15, 20, 30, 40, 50, 60]
    # number_list = [1000, 5000, 10000, 50000, 100000]
    # type_list = [0, 1]


    #num_circles = int(random(3,20))
    # num_circles = 1
    # for i in range(num_circles):
        # radius = random_list_value(radius_list)
        # spread = random_list_value(spread_list)
        # number = random_list_value(number_list)
        
        # radius = int(random(20, 300))
        # spread = int(random(3, 50))
        # type = random_list_value(type_list)
        
        # radius = 200
        # spread = 20
        # type = 1
        

        # if type == 0:
        #     type = 'dots'
        #     number = int(random(50000, 100000))
        #     circle_dots(hsba=(0, 0, 0, 5), number=number, radius=(radius, radius), spread=[spread])
        # elif type == 1:
        #     type = 'lines'
        #     # number = int(random(100, 5000))
        #     # center = int(random(0, 20))
        #     number = 100000
        #     center = 0
        #     circle_lines(hsba=(0, 0, 0, 5), number=number, radius=(radius, radius), spread=[spread], center_offset=center)
            
        # print('num: {}, type: {}, radius: {}, spread: {}, number: {}'.format(num_circles, type, radius, spread, number))
        # fill(color(0, 0, 0, 100))
        # ellipse(w/2, h/2, 2*radius, 2*radius)
        
        # fill(color(0, 0, 100, 100))
        # ellipse(w/2, h/2, radius, radius)
        
    # noFill()
    # ellipse(w/2, h/2, 160, 160)
    # ellipse(w/2, h/2, 240, 240)


    # Dot circles (looks like spraypaint)
    # for spread in [5, 7, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20]:
    #     circle_dots(hsba=(0, 0, 0, 5), number=100000, spread=spread, stroke_weight=0.7)
        
    #circle_lines(hsba=(0, 0, 0, 5), center=(w/2,h/2), number=1000, radius=(150, 150), spread=20, stroke_weight=0.5)
    #circle_lines(hsba=(0, 0, 0, 5), center=(w/2,h/2), number=3000, radius=(400, 400), spread=50, stroke_weight=0.5)
    
    # Dot circles (looks like spraypaint)
    # spread = [5, 7, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20]
    # spread = [10]
    # circle_dots(hsba=(0, 0, 0, 5), number=1000000, radius=(160, 160), spread=spread, stroke_weight=0.7)
    # circle_dots(hsba=(0, 0, 0, 5), number=1000000, radius=(240, 240), spread=spread, stroke_weight=0.7)
    #circle_dots(hsba=(0, 0, 0, 5), number=100000, radius=(300, 300), spread=spread, stroke_weight=0.7)
    
    # noStroke()
    # fill(g.backgroundColor)
    # ellipse(w/2, h/2, 230, 230)
    
    
    # spread = [20]
    # circle_lines(hsba=(0, 0, 0, 5), number=5000, radius=(200, 200), spread=spread, stroke_weight=0.7)
    
    #border()
    filename = create_filename('test')
    saveFrame('output/blur_circles_######.png')
    #print('concentric_{:02}_{:02}_{:01}.png'.format(num_circles, num_cols, int(xy_noise*10)))

def random_list_value(val_list):
    index = int(random(0, len(val_list)))
    value = val_list[index]
    return value
        
        
def circle_dots(hsba=(0, 50, 50, 50), center=(w/2,h/2), number=100, radius=(200,200), spread=[10], stroke_weight=0.7):
    for s in spread:
        for i in range(number):
            r_offset = randomGaussian()*s
            x = center[0] + (radius[0] + r_offset) * cos(TWO_PI * i / number) 
            y = center[1] + (radius[1] + r_offset) * sin(TWO_PI * i / number)
            strokeWeight(stroke_weight)
            stroke(color(*hsba))
            point(x, y)
        
def circle_lines(hsba=(0, 50, 50, 50), center=(w/2,h/2), number=100, radius=(200, 200), spread=[10], stroke_weight=0.7, center_offset=10):
    for i in range(number):
        r_offset = randomGaussian()*spread[0]
        d_x = 2*radius[0] + r_offset
        d_y = 2*radius[1] + r_offset
        noFill()
        strokeWeight(stroke_weight)
        stroke(color(*hsba))
        ellipse(center[0]+randomGaussian()*center_offset, center[1]+randomGaussian()*center_offset, d_x, d_y)
    
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
    
    



    
