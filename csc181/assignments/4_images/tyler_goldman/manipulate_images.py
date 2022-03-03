import os
from os import path
from PIL import Image as pil_image


file_path = os.path.dirname(os.path.realpath(__file__))
source_path = os.path.join(file_path, 'images')
dest_path = os.path.join(file_path, 'newImages')


if not os.path.isdir(source_path):
    print('hello')
    os.makedirs(source_path)

if not os.path.isdir(dest_path):
    os.mkdir(dest_path)

count = 0
new_name =''
for file_name in os.listdir(source_path):
    with open(os.path.join(source_path,file_name)) as people_file:
        image = pil_image.open(os.path.join(source_path, file_name))
        print(image.size)
        image = image.resize((75,75))   
        image = image.rotate(270) 
        image = image.convert('L')
        if(count < 10):
            new_name='pic000' + str(count) + '.png'
            count+=1
        elif(count < 100):
            new_name='pic00' + str(count) + '.png'
            count+=1
        elif(count >= 100):
            new_name='pic0' + str(count) + '.png'
            count+=1
        image.save(os.path.join(dest_path, new_name))
        print(image.size)