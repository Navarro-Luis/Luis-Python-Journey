#jpg to PNG Converter!!
import sys
import os
from PIL import Image

#grab first and second argument(existing fodler and new folder)
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new/ exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
#loop thru pokedex

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0] #remove the .jpg name on file

    #convert each image to png

    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done!')
#save to the new folder
