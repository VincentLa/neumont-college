# Will require something like
# /Users/vincentla/.pyenv/versions/3.9.7/bin/python -m pip install Pillow
# in terminal.
# Hopefully just pip install works for most users.
from PIL import Image as pil_image
import os

# Setup paths
file_path = os.path.dirname(os.path.realpath(__file__))
source_path = os.path.join(file_path, 'images')
dest_path = os.path.join(file_path, 'dest')

# Create source path if not exists
if not os.path.isdir(source_path):
    print('hello')
    os.makedirs(source_path)

# Create source path if not exists
if not os.path.isdir(dest_path):
    os.makedirs(dest_path)

# Read all the files in the source folder
files = os.listdir(path=source_path)

print(files)

if len(files) > 0:
    file = files[0]

    image = pil_image.open(os.path.join(source_path, file))

    print(image.size)

    image = image.rotate(270)        

    image.save(os.path.join(dest_path, file))

    # Students need to research and discover how to manipulate the image


