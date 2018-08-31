################################################################################
# concentric_iterative
#
# Playing around with concentric circles and sweeping through parameters
# 
# Based on the talented Paul Rickards: 
# https://twitter.com/paulrickards/status/1028651749555560448
#
# Aaron Penne 
# 2018-08-21
# https://github.com/aaronpenne
################################################################################


# Define globals here
rand_seed = 1138
frame_rate = 1

w = 600  # width
h = 800  # height

width_square = 20

num_cols = 7
num_rows = 0

pad = h/2
pad_pct = 0.11

# Colors from https://www.instagram.com/p/BmBXtByF_Kn/
colors_hex = ['#20222f',  # Black
              '#20222f',  # Black
              '#20222f',  # Black
              '#20222f',  # Black
              '#20222f',  # Black
              '#1a1f56',  # Dark Violet 1/8
              '#2c1e7d',  # Violet 2/8
              '#0134aa',  # Darkest Blue 3/8
              '#0060e8',  # Dark Blue 4/8
              '#0297fb',  # Blue 5/8
              '#00befa',  # Blue 6/8
              '#83def3',  # Light Blue 7/8
              '#d1ecf7',  # Lightest Blue 8/8
              '#f2f6f9',  # White
              '#f2f6f9',  # White
              '#f2f6f9',  # White
              '#fce503',  # Yellow
              '#fe6d02',  # Orange
              '#e7011d',  # Red
              '#4b0f31',  # Dark Red
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
        
    # Set the psuedorandom seed
    #randomSeed(rand_seed)
    
    # Set (x, y) for circles to center
    ellipseMode(CENTER)
    
    
    background(0, 0, 97)
    
    global colors_hex, num_rows
    num_rows = height/width_square
    while num_rows > len(colors_hex):
        colors_hex += colors_hex
        print(colors_hex)
    colors_hex += colors_hex
    
    # Stops draw() from running in an infinite loop (should be last line)
    noLoop()



def draw():
    
    #num_circles = 11
    
    #num_cols = 6
    
    #y_noise = 0.03
    #x_noise = 0.02

    num_cols = int(width / width_square)
    num_straight_left = int(num_cols * 0.2)
    num_straight_right = int(num_cols * 0.1)
    for x in range(num_straight_left):
        color_bar(x*width_square)
    offset_angle = x-num_straight_left
    for x in range(num_straight_left, num_cols-num_straight_right):
        if int(random(0,2)):
            offset_angle = x-num_straight_left
            if int(random(0,2)):
                offset = offset_angle + int(random(-5, 5))
            else:
                offset = offset_angle
            color_bar(x*width_square, offset)
        else:
            
    for x in range(num_cols-num_straight_right, num_cols):
        color_bar(x*width_square, offset_angle)

    #border()
    #annotate(num_circles, num_cols, xy_noise)
    #saveFrame('output/concentric_{:02}_{:02}_{:01}.png'.format(num_circles, num_cols, int(xy_noise*10)))
    #print('concentric_{:02}_{:02}_{:01}.png'.format(num_circles, num_cols, int(xy_noise*10)))

def color_bar(x=0, offset=0, colors=colors_hex):
    
    num_colors = len(colors)
        
    idx_colors = offset
    for i in range(num_rows):
        y = i*width_square
        print(idx_colors, num_colors)
        if idx_colors >= num_colors:
            idx_colors = offset
        else:
            idx_colors += 1
        fill(colors_hex[idx_colors])
        noStroke()
        rect(x, y, width_square, width_square)
        
def border():
    noStroke()
    fill(g.backgroundColor)
    rect(0, 0, width, height*pad_pct)  # Top
    rect(0, 0, width*pad_pct, height)  # Left
    rect(0, height - height*pad_pct, width, height*pad_pct)  # Bottom
    rect(width - width*pad_pct, 0, width*pad_pct, height)  # Right
    
def annotate(num_circles, num_cols, xy_noise):
    stroke(0)
    fill(0)
    textFont(createFont('Courier',100))
    textAlign(LEFT, TOP)
    textSize(height*0.013)
    text('concentric_{:02}_{:02}_{:01}.png\nEmulating @paulrickards'.format(num_circles, num_cols, int(xy_noise*10)), width*pad_pct, height - (height*pad_pct*0.9))
    textAlign(RIGHT, TOP)
    text('Aaron Penne', width - width*pad_pct, height - (height*pad_pct*0.9))
    
    
