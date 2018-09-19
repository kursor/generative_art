################################################################################
# Lines
# -----
#
# Playing around with moving lines in object oriented fashion.
# Just getting familiar.
# Based on this example: https://processing.org/examples/setupdraw.html
#
# Aaron Penne 
# 2018-08-21
# https://github.com/aaronpenne
################################################################################

# Define globals here
seed = 1138
x = 777
w = 400  # width
h = 600  # height
pad = h/2
pad_pct = 0.07

class Hline(object):
    def __init__(self, weight=1, y=0, speed=1, direction=-1, c='#ffffff'):
        self.weight = weight
        self.y = y
        self.speed = speed
        self.direction = direction
        self.c = c
        
    def move(self):
        self.y = self.y + (self.speed * self.direction)
        if self.y < 0 - pad:
            self.y = height
        elif self.y > height + pad:
            self.y = 0
        
    def display(self):
        stroke(self.c)
        strokeWeight(self.weight)
        line(0, self.y, width, self.y)
        
        
randomSeed(seed)

# all_directions = [-1, 1]
line_dict = {}
hue_dict = {}
alpha_dict = {}
line_range = 100
for x in range(50, line_range):
    weight = random(0, 10)
    y = 0
    speed = random(0.5, 4)
    # direction = all_directions[int(random(0,2))]
    line_dict[x] = Hline(weight, y, speed)
    hue_dict[x] = random(0,360)
    alpha_dict[x] = random(30,6)

def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)
        
    # Set the number of frames per second to display
    frameRate(100)
        
    # Set the psuedorandom seed
    randomSeed(seed)
    
    # Stops draw() from running in an infinite loop (should be last line)
    # noLoop()

def draw():
    background(0, 0, 24.7)
    for x in range(50, line_range):
        line_dict[x].c = color(0, 0, 100, alpha_dict[x])
        line_dict[x].move()
        line_dict[x].display()
    border()
        
def border():
    noStroke()
    fill('#ffffff')
    rect(0, 0, width, height*pad_pct)  # Top
    rect(0, 0, width*pad_pct, height)  # Left
    rect(0, height - height*pad_pct, width, height*pad_pct)  # Bottom
    rect(width - width*pad_pct, 0, width*pad_pct, height)  # Right
