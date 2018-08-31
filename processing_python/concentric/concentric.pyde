################################################################################
# Concentric
#
# Playing around with concentric circles
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
x = 777
w = 400  # width
h = 600  # height
pad = h/2
pad_pct = 0.07


        
        
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
    
    
    background(0, 0, 24.7)
    
    # Stops draw() from running in an infinite loop (should be last line)
    noLoop()



def draw():
    concentric_circles()
    border()
    
def concentric_circles(x=100, y=100, num_circles=3, outer_radius=100, color_fill='#ffffff', color_stroke='#000000', weight=1):
        step = outer_radius / num_circles
        radius = outer_radius
        for i in range(0,num_circles+1):
            print(i, radius)
            ellipse(x, y, radius, radius)
            radius -= step
        
def border():
    noStroke()
    fill('#ffffff')
    rect(0, 0, width, height*pad_pct)  # Top
    rect(0, 0, width*pad_pct, height)  # Left
    rect(0, height - height*pad_pct, width, height*pad_pct)  # Bottom
    rect(width - width*pad_pct, 0, width*pad_pct, height)  # Right
