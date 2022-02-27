from PIL import Image, ImageOps
import os

filePath = os.path.dirname(os.path.realpath(__file__))
sourcePath = os.path.join(filePath, 'images')
destPath = os.path.join(filePath, 'newImages')

assert os.path.isdir(sourcePath)

if not os.path.isdir(destPath):
    print("Creating Folder: {}".format(destPath))
    os.mkdir(destPath)

imagePaths = list()

for imDir in os.listdir(sourcePath):
    imagePaths.append(os.path.join(sourcePath, imDir))

for idx, imDir in enumerate(imagePaths):
    print(imDir)
    with Image.open(imDir) as im:
        width, height = im.size
        
        # im = im.crop((0, 0, (width - (width - height)), height))       
        im = im.rotate(270)
        im = im.crop((0, 0, 75, 75))
        print(im.size)
        im = ImageOps.grayscale(im)
        
        fileName = 'pic' + str(idx+1).zfill(4) + ".png"
        im.save(os.path.join(destPath, fileName))

    
