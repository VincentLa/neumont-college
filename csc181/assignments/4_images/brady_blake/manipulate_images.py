from PIL import Image as pil_image
import os, sys

file_path = os.path.dirname(os.path.realpath(__file__))
source_path = os.path.join(file_path, 'images')
dest_path = os.path.join(file_path, 'new_images')

# Create source path if not exists
if not os.path.isdir(source_path):
    print('hello')
    os.makedirs(source_path)

# Create dest path if not exists
if not os.path.isdir(dest_path):
    os.makedirs(dest_path)

# Read all the files in the source folder
files = os.listdir(path=source_path)

for file in files:
    
    images = pil_image.open(os.path.join(source_path, file))

    f, e = os.path.splitext(file)
    image = f + ".png"
    print(image, file)
    # if image != file:
    #     try:
    #         with images as inf:
    #             print('hello')
    #             # inf.save(image)
    #     except OSError:
    #         print("Cannot convert", inf)        

    print(images.size)

    images.rotate(270) 
       
    images.save(os.path.join(dest_path, file))
