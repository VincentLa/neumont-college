from PIL import Image as pil_image
import os

os.system('cls')

# Setup paths
source_path = './2-GUI/images/'
dest_path = './2-GUI/dest/'

# Create source path if not exists
if not os.path.isdir(source_path):
    os.mkdir(source_path)

# Create source path if not exists
if not os.path.isdir(dest_path):
    os.mkdir(dest_path)

# Read all the files in the source folder
files = os.listdir(path = source_path)

if len(files) > 0:
    file = files[0]

    image = pil_image.open(source_path + file)

    print(image.size)

    image = image.rotate(270)        

    image.save(dest_path + file)

    # Students need to research and discover how to manipulate the image


