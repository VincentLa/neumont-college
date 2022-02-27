from PIL import Image, ImageChops, ImageOps
import os

file_path = os.path.dirname(os.path.realpath(__file__))
source_path = os.path.join(file_path, 'images')
des_path = os.path.join(file_path, 'new_images')

if not os.path.isdir(des_path):
    os.makedirs(des_path)

def trim(im, border):
    bg = Image.new(im.mode, im.size, border)
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    else:
        # found no content
        raise ValueError("cannot trim; image was empty")
y = 0
for x in os.listdir(source_path):
    image = Image.open(os.path.join(source_path, x))
    image = image.rotate(-90)
    image = trim(image, 0)
    image = ImageOps.contain(image, (75, 75))
    image = ImageOps.grayscale(image)
    image.save(os.path.join(des_path, "pic{:0>4}.png".format(y)))
    y += 1






