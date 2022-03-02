from typing import Counter
from PIL import Image as pil_image
from PIL import ImageOps as im1
import os 

file_path = os.path.dirname(os.path.realpath(__file__))
filePath = os.path.join(file_path, "images")
newPath = os.path.join(file_path, "new images")

if not os.path.isdir(newPath):
    os.mkdir(newPath)

files = os.listdir(path = filePath)
counter = 1
cropTool = ()

for img in files:
    print(img)
    image = pil_image.open(os.path.join(filePath, img))
    width, height = image.size
    
    left = 5
    top = height / 4
    right = 164
    bottom = 3 * height / 4
    image.crop((left, top, right, bottom))
    
    image.rotate(90)
    
    pixels = (75,75) 
    image.thumbnail(pixels)
    im1.grayscale(image)
    
    savePic = os.path.join(newPath, f"pic{str(counter).rjust(4, '0')}.png")
    
    print(f"Saving {img} as {savePic}")
    image.save(savePic)
    
    counter += 1
    
    if counter > 300:
        break
