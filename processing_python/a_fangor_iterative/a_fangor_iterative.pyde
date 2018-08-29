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

color_dict = {0: [[180, 100, 100],  #00ffff cyan
                  [300, 100, 100],  #ff00ff magenta
                  [60, 100, 100],   #ffff00 yellow
                  [0, 0, 0],        #000000 black
                  [0, 0, 100]        # background
                  ],
              # From Warhol's Mick Jagger
              1: [[41, 41, 66],  #a99364 brown  
                  [342, 32, 85], #da95aa pink
                  [45, 7, 96],   #f4f0e4 cream
                  [354, 60, 72], #b74954 red
                  [98, 19, 87],  #c2ddb2 green
                  [0, 0, 100]     # background
                  ],
              # From Van Gogh's Bedroom
              2: [[225, 61, 55], #374D8D blue
                  [226, 28, 80], #93A0CB light blue
                  [95, 39, 66],  #82A866 green
                  [54, 66, 77],  #C4B743 yellow
                  [19, 75, 64],  #A35029 dark orange
                  [0, 0, 100]     # background
                  ],
              # From JMW Turner's Mountain Scene
              3: [[51, 15, 95],  #F1ECCE cream
                  [227, 13, 71], #9EA3B5 gray
                  [48, 42, 91],  #E9D688 tan
                  [18, 68, 66],  #A85835 dark orange
                  [34, 60, 68],  #AE8045 brown
                  [0, 0, 100]     # background
                  ],
              # Just blue and white
              4: [[198, 62, 75],
                  [0, 0, 100]
                  ],
              # Just black and white
              5: [[0, 0, 5],
                  [0, 0, 100]
                  ],
              # Just red and white
              6: [[348, 63, 84],
                  [0, 0, 100]
                  ],
              }
palettes = ['cmyk', 'warhol', 'van_gogh', 'turner', 'blue', 'black', 'red']            


def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)
        
    # Set the number of frames per second to display
    frameRate(frame_rate)
    
    # Set (x, y) to center
    imageMode(CENTER)
    ellipseMode(CENTER)
    textMode(CENTER)
    rectMode(CENTER)
    
    background(0, 0, 97)
    
    # Stops draw() from running in an infinite loop (should be last line)
    #randomSeed(rand_seed)
    #noLoop()



def draw():
    global count
    if count > 5000:
        sys.exit(0)
    count += 1

    background(0, 0, 100)
    
    idx = int(random(0, len(color_dict.keys())))
    color_list = color_dict[idx]
    palette = palettes[idx]
    
    #type = random_list_value(['ellipse', 'rect'])
    type = 'ellipse'
    
    offset = 3
    
    pg = createGraphics(w, h)
    pg.beginDraw()
    pg.noStroke()
    pg.background(0, 0, 100, 0)
    
    pg.ellipseMode(CENTER)
    pg.rectMode(CENTER)
    
    num_circles = int(random(2, 8))
    radii = [int(random(0, 300)) for x in range(num_circles)]
    radii = sorted(radii, reverse=True)
    
    c = None
    annotation = []
    for i,r in enumerate(radii):
        idx = int(random(0, len(color_list)))
        if c != color(*color_list[idx]):
            c = color(*color_list[idx])
            pg.fill(c)
            if type == 'ellipse':
                pg.ellipse(w/2, h/2, 2*r, 2*r)
            elif type == 'rect':
                pg.rect(w/2, h/2, 2*r, 2*r)
            
            annotation.append(['r:{}, h:{}, s:{}, b:{}'.format(r, color_list[idx][0], color_list[idx][1], color_list[idx][2])])
            
    pg.endDraw()
    if random_list_value([True, False]):
        print('hi')
        image(pg, width/2, height/2)
    blur = int(random(3, 30))
    pg.filter(DILATE)
    pg.filter(BLUR, blur)
    
    image(pg, width/2, height/2)
    
    pad = 10
    mono = createFont('Monospaced', 100)
    textFont(mono)
    textSize(pad)
    fill(0, 0, 0)
    text(palette, 10, 10)
    for i,notes in enumerate(annotation):
        text(notes[0], 10, 20+i*pad)
    
    print(count)
    filename = create_filename('test')
    saveFrame('output/blur_circles_{}_#######.png'.format(palette))
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

def pg_circle_dots(pg, hsba=(0, 50, 50, 50), center=(w/2,h/2), number=100, radius=(200,200), spread=[10], stroke_weight=0.7):
    pg.beginDraw()
    for s in spread:
        for i in range(number):
            r_offset = randomGaussian()*s
            x = center[0] + (radius[0] + r_offset) * cos(TWO_PI * i / number) 
            y = center[1] + (radius[1] + r_offset) * sin(TWO_PI * i / number)
            pg.strokeWeight(stroke_weight)
            pg.stroke(color(*hsba))
            pg.point(x, y)
    pg.endDraw()
        
def pg_circle_lines(pg, hsba=(0, 50, 50, 50), center=(w/2,h/2), number=100, radius=(200, 200), spread=[10], stroke_weight=0.7, center_offset=10):
    pg.beginDraw()
    for i in range(number):
        r_offset = randomGaussian()*spread[0]
        d_x = 2*radius[0] + r_offset
        d_y = 2*radius[1] + r_offset
        pg.noFill()
        pg.strokeWeight(stroke_weight)
        pg.stroke(color(*hsba))
        pg.ellipse(center[0]+randomGaussian()*center_offset, center[1]+randomGaussian()*center_offset, d_x, d_y)
    pg.endDraw()
    
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
    
    



    
