import os
import imageio

png_files = os.listdir()
png_files = [x for x in png_files if x.endswith('.png')]
png_files = sorted(png_files)

images = []
for filename in png_files:
    images.append(imageio.imread(filename))
imageio.mimsave('output.gif', images, format='GIF', duration=1)
