import os

from PIL import Image, ImageOps

# Setup Paths
file_path = os.path.dirname(os.path.realpath(__file__))
source_path = os.path.join(file_path, 'images')
dest_path = os.path.join(file_path, 'new_images')

# Create the directory if it doesn't exist
if not os.path.isdir(dest_path):
    print("Creating folder: {}".format(dest_path))
    os.makedirs(dest_path)

def main():
    for count, filename in enumerate(os.listdir(source_path)):
        # Getting path
        image = Image.open(os.path.join(source_path, filename))
        # Rotating
        image = image.rotate(-90)
        # Cropping image
        image = image.crop((25,0, 225, 200))
        # Resizing Image
        image = image.resize((75,75))
        # grayscale
        image = ImageOps.grayscale(image)

        dstName = f"pic{str(count + 1).zfill(4)}.png"
        image.save(os.path.join(dest_path, dstName))

if __name__ == '__main__':
    main()
