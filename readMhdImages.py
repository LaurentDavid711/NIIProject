# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 15:23:18 2016

@author: L.David
"""
import mhd_browse

def main(): 
    """
    Entry point of the code. Given a base directory, and optional filters, the script recovers all the .mhd files in the directory.
    
    """
    directorySearch = raw_input("Please select:\n 1 to set directory in the current folder.\n 2 to choose the directory manually.\n")
    if directorySearch == "1":
        rootDirectory = ".."
    else : 
        rootDirectory = raw_input('Enter directory : ')

    itype = raw_input('Enter image type (type q to ignore, example: Wild) : ')
    name = raw_input('Enter base name (type q to ignore, example: COMSCAN): ')
    if itype == "q":
        if name == "q":
            images = mhd_browse.readAllImages(rootDirectory)
        else : 
            images = mhd_browse.readAllImages(rootDirectory, baseName = name)
    else : 
        if name == "q":
            images = mhd_browse.readAllImages(rootDirectory, imageType = itype)
        else :
            images = mhd_browse.readAllImages(rootDirectory, imageType = itype , baseName = name)
    print("All files read.")
    # Work on the images
    # example :
    # directory: "H:\NII\Backup\Sharmili"
    #print(images[0].header)
    return images


if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it

