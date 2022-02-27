import os
from PIL import Image

file_path = os.path.dirname(os.path.realpath(__file__))
source_pth = os.path.join(file_path, "images")
dest_path = os.path.join(file_path, "new images")

if not os.path.isdir(dest_path):
    print("making folder {}".format(dest_path))
    os.makedirs(dest_path)

images=os.listdir(source_pth)
#image=Image.open(os.path.join(source_pth,"aagib.jpg"))

for num, imagename in enumerate(images):
    image=Image.open(os.path.join(source_pth, imagename))
    image=image.rotate(-90, expand=True)
    image=image.resize((75, 75))
    print(image.size)
    image=image.convert("L")
    image.save(os.path.join(dest_path, "pic" + str(num).zfill(4) + ".png"))