from PIL import Image
import os
import sys

#Setup Paths
file_path = os.path.dirname(os.path.realpath(__file__))
source_path = os.path.join(file_path, 'images')
dest_path = os.path.join(file_path, 'new_images')

#Create a directory if it doesn't exist
if not os.path.isdir(dest_path):
    print("Creating folder: {}".format(dest_path))
    os.makedirs(dest_path)

#Rename in Bulk
files = os.listdir(source_path)
for index, file in enumerate(files):  

    #Loading the image
    image = Image.open(os.path.join(source_path, file))

    #Rotating the Image
    image = image.rotate(-90)

    #Grayscale the image
    image =  image.convert('LA')

    #Crop image
    left = 25
    top = 0
    right = 225
    bottom = 200
    image = image.crop((left, top, right, bottom))

    #Resize image
    width, height = image.size
    newsize = (75, 75)
    image = image.resize(newsize)

    #Save the resulting image
    image.save(os.path.join(dest_path,  'pic' + str(f"{index:04d}" + '.png')))
    


