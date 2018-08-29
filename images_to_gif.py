import os
import sys
import imageio
import argparse
import datetime

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='Convert images in a directory to gif.\nDefaults to png files in current directory.')
parser.add_argument('-d', '--dir', help='directory containing image files')
parser.add_argument('-f', '--format', help='image format to be converted to gif')
parser.add_argument('-t', '--time', type=float, help='number of seconds to display single image')
args = parser.parse_args()

if not args.dir:
    args.dir = '.'

if not args.format:
    args.format = 'png'

if not args.time:
    args.time = 1

image_files = os.listdir(args.dir)
image_files = [x for x in image_files if x.lower().endswith(args.format.lower())]
image_files = sorted(image_files)

if not image_files:
    print(f'No {args.format.lower()} files found')
    sys.exit(0)

images = []
image_shape = 0
for filename in image_files:
    image = imageio.imread(os.path.join(args.dir, filename))
    images.append(image)
    print(filename, image.shape)
    if (image_shape != image.shape) and (image_shape != 0):
        print('ERROR: image shapes are not consistent')
        sys.exit(0)
    image_shape = image.shape

print('Creating gif...')
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
imageio.mimsave(f'_{timestamp}.gif', images, format='GIF', duration=args.time)
