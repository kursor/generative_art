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

x_pad = 10
theta = 0
amplitude = 100

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
    noLoop()



def draw():
    global count
    if count > 5000:
        sys.exit(0)
    count += 1

    background(0, 0, 100)
    
    palette_name, palette = select_palette(idx=0)
    print(palette_name)
    # c = palette[3]
    # print(c)

    x = []
    for x_val in range(0, width, x_pad):
        x.append(x_val) 
    x_tmp = normalize_list(x, 0, 1)
    x_norm = [0]*len(x_tmp)
    pad = int(len(x_tmp)/3)
    x_norm[pad:] = x_tmp[0:len(x_tmp)-pad]
    print(x_norm)
    
    
    sins = [abs(sin(v*2*math.pi)**2) for v in x_tmp]   
    x_start_perturb_max = 5
    x_end_perturb_max = 5
    y_start_perturb_max = 3 
    y_end_start_perturb_max = 15 
    
    for ix, x_val in enumerate(range(0, width, x_pad)):
        for iy, y_offset in enumerate(range(0, height, height/100)):
            #horizontal_wave = (int(sin(y_offset/float(height)*2*math.pi)*0.25*len(sins)))
            horizontal_wave = 1
            phase = (horizontal_wave + (ix/2 + iy/3))%len(sins)
            y_start_randomness = random(-y_start_perturb_max, y_start_perturb_max)*sins[phase]
            y_end_randomness = random(-y_end_start_perturb_max, y_end_start_perturb_max)*sins[phase]
            x_start_randomness = random(0, x_start_perturb_max)*sins[phase]+1
            x_end_randomness = random(-x_end_perturb_max, 0)*sins[phase]-1
            line(x_val+x_start_randomness, y_offset+y_start_randomness, x_val+x_end_randomness+x_pad, y_offset+y_end_randomness) # x_norm[ix])
            
    output_filename = os.path.join('output', 'sinful_#######.png')
    filename = create_filename('sinful')
    saveFrame(output_filename)
    print(output_filename)

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
    

def normalize_list(val_list, a, b):
    a = float(a)
    b = float(b)
    normalized = []
    for val in val_list:
        normalized.append((b - a) * (val - min(val_list)) / (max(val_list) - min(val_list)) + a)
    return normalized

def select_palette(idx=None):
    print(idx)
    palettes = ['cmyk', 'warhol', 'van_gogh', 'turner', 'blue', 'black', 'red']  
    color_dict = {0: [[180, 100, 100], #00ffff cyan
                  [300, 100, 100],     #ff00ff magenta
                  [60, 100, 100],      #ffff00 yellow
                  [0, 0, 0],           #000000 black
                  [0, 0, 100]          # background
                  ],
              # From Warhol's Mick Jagger
              1: [[41, 41, 66],   #a99364 brown  
                  [342, 32, 85],  #da95aa pink
                  [45, 7, 96],    #f4f0e4 cream
                  [354, 60, 72],  #b74954 red
                  [98, 19, 87],   #c2ddb2 green
                  [0, 0, 100]     # background
                  ],
              # From Van Gogh's Bedroom
              2: [[225, 61, 55], #374D8D blue
                  [226, 28, 80], #93A0CB light blue
                  [95, 39, 66],  #82A866 green
                  [54, 66, 77],  #C4B743 yellow
                  [19, 75, 64],  #A35029 dark orange
                  [0, 0, 100]    # background
                  ],
              # From JMW Turner's Mountain Scene
              3: [[51, 15, 95],  #F1ECCE cream
                  [227, 13, 71], #9EA3B5 gray
                  [48, 42, 91],  #E9D688 tan
                  [18, 68, 66],  #A85835 dark orange
                  [34, 60, 68],  #AE8045 brown
                  [0, 0, 100]    # background
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

    # Select random color palette if none specified
    if idx is None:
        idx = int(random(0, len(color_dict.keys())))
    palette_name = palettes[idx]
    palette = color_dict[idx]
    
    return palette_name, palette
    
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
    
    



    
