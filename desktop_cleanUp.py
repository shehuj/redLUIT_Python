# Make the folder cleanedUp/ folder
# List the files in the Desktop/ folder
# For each file in the Desktop/ folder
# move the file to the cleanedUp/ folder


import os
#import time
#import random   
#import shutil

# folder = input("Enter the path of the folder to clean up: \n")
folder_original = "/Users/captcloud01/Desktop"
# Example: folder = "/Users/captcloud01/Desktop"
folder_destination = "/Users/captcloud01/Desktop/Sorted"

os.mkdir(folder_destination)

for entry in os.scandir(folder_original):

    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)
    
    if os.path.isfile(location_original):
           os.rename(location_original, location_destination)

