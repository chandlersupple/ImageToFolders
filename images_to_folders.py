# Date: June 28, 2018
# Author: Chandler Supple
# File: 'images_to_folders.py'

import os
import os.path
import shutil
import pandas as pd

labels = pd.read_csv('labels.csv') # Image labels -- should consist of two columns: 'Id' (containing labels), 
# 'Image' (containing image names (ie. 'cat.png')

images_folder = '(Folder Path)' # Images will be pulled from this folder
storing_folder = '(Folder Path)' # The resulting folders of images will be dumped here

for image in range (len(labels['Id'])):
    
    img_id = labels['Id'][image] # Image label
    img_name = labels['Image'][image] # Name of image (ie. 'dog.png')
    
    storing_folder_in = os.path.join(storing_folder, img_id)
    if not os.path.exists(storing_folder_in): 
        os.makedirs(storing_folder_in) # Makes a new folder if the name is unique and has not been made

    current_image_path = os.path.join(images_folder, img_name)
    target_image_path = os.path.join(storing_folder_in, img_name)
    shutil.move(current_image_path, target_image_path)
