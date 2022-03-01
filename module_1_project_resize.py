#!/usr/bin/python3
from PIL import Image
import os


inpath = 'c:\\Users\\Miro\\My Drive\\Python_coursera\\6 Automating real world tasks\\Testing_images\\'

outpath = 'c:\\Users\\Miro\\My Drive\\Python_coursera\\6 Automating real world tasks\\Testing_images_done\\'


# Check whether the outpath exists or no
isExist = os.path.exists(outpath)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(outpath)
  print("The new directory is created!")


for images in os.listdir(inpath):
    # imagePath contains name of the image 
    inputpath = os.path.join(inpath, images)
  
    # inputPath contains the full directory name
    img = Image.open(inputpath)
  
    fullOutPath = os.path.join(outpath, 'invert_' + images + '.png')
    # fullOutPath contains the path of the output
    # image that needs to be generated
    img.rotate(90).resize((640,480)).save(fullOutPath) 
