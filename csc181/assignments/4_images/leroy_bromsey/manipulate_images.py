from typing import Counter
from PIL import Image as pil_image
from PIL import ImageOps as im1
import os 

file_path = os.path.dirname(os.path.realpath(__file__))
source_path = os.path.join(file_path, 'images')
des_path = os.path.join(file_path, 'new_images')

if not os.path.isdir(des_path):
    os.mkdir(des_path)

files = os.listdir(path = source_path)
counter = 1

crop_box = ()

for img in files:
    print(img)
    image = pil_image.open(os.path.join(source_path, img))
    
    width, height = image.size
    
    left = 5
    
    top = height / 4
    
    right = 164
    
    bottom = 3 * height / 4
    
    image = image.crop((left, top, right, bottom))
    
    image = image.rotate(90)
    
    pixels = (75,75) 
    image.thumbnail(pixels)
    
    
    image = im1.grayscale(image)
    
    
    
    
    save_image = os.path.join(des_path, f"pic{str(counter).rjust(4, '0')}.png")
    
    print(f"Saving {img} as {save_image}")
    image.save(save_image)
    
    counter += 1
    
    if counter > 300:
        break

