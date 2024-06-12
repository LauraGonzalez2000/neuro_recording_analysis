import numpy as np
import matplotlib.pylab as plt
import os

from igor2.packed import load as loadpxp

#data = loadpxp('C:/Users/laura.gonzalez/DATA/nm28May2024c0/nm28May2024c0_000.pxp')

#files = os.listdir('C:/Users/laura.gonzalez/DATA')
#for file in files:
#    if 'nm' in file:
#        print('- ', file)


#data = loadpxp('C:/Users/laura.gonzalez/DATA/nm28May2024c0/nm28May2024c0_000.pxp')
#print('hey', data, 'hey')


def find_nm_files(root_folder):
    nm_paths = []
    
    # Walk through all directories and files in the root_folder
    for folder, _, files in os.walk(root_folder):
        # Check each file in the current directory
        for file in files:

            # Skip files with specific extensions
            if any(ext in file for ext in ['HDF5', 'txt', 'pdf', 'log', 'xlsx']):
                break
            # Construct the full path of the file
            file_path = os.path.join(folder, file)
            normalized_path = os.path.normpath(file_path)
            forward_slash_path = normalized_path.replace("\\", "/")
            nm_paths.append(forward_slash_path)
            print('-', file)

    return nm_paths

def load_data(file):
    try:
        data = loadpxp(file)
        print("data was loaded")
    except:
        print("data was not loaded")

###### MAIN

files = find_nm_files('C:/Users/laura.gonzalez/DATA/RAW_DATA')
for file in files:
    data = load_data(file)
    #analyse each file to create a pdf

    #analyse each file to create excel

    #analyse each file to plot


'''
print('C:/Users/laura.gonzalez/DATA/nm03Jun2024c0/nm03Jun2024c0_000.pxp')
print(files[0])
print(str(files[0]))

data = loadpxp('C:/Users/laura.gonzalez/DATA/nm28May2024c0/nm28May2024c0_000.pxp')
print(data)
#data = loadpxp(str(files[0]))
#print(data)
'''
