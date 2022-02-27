import os

from PIL import Image 

# Setup Paths
file_path = os.path.dirname(os.path.realpath(__file__))
source_path = os.path.join(file_path, 'images')
dest_path = os.path.join(file_path, 'new_images')

# Create a directory if it doesn't exist
if not os.path.isdir(dest_path):
    print("Creating folder: {}".format(dest_path))
    os.makedirs(dest_path)

# Loading the image
image = Image.open(os.path.join(source_path, 'aagib.jpg')) 

# What's the size of the image in pixels?
print(image.size)

# Rotating the Image
image = image.rotate(270)

rgb_image = image.convert('RGB')
print('Printing RGB Value of pixel in 1,1')
print(rgb_image.getpixel((1,1)))

grey_image = PIL.ImageOps.grayscale(image)

# Save the resulting image to the destination path
image.save(os.path.join(dest_path, 'new_aagib.jpg'))    