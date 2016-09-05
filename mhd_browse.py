# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 12:42:39 2016

@author: L.David
"""
import os
import Mhd_Structure

def findImages(baseDirectory):
    """
    Returns an array with the directory and name of all .mhd files in the baseDirectory
    Example: output =   [['path1', 'image1'],
                         ['path2', 'image2']]
    """
    directories = []
    fileType = ".mhd"
    # Browse all directories
    for root, dirs, files in os.walk(baseDirectory):
        for file in files:
            if file.endswith(fileType):
                # Add path and file name to the output
                directories.append([root, file])
    return directories

def readAllImages(baseDirectory, imageType = "", baseName = ""):
    """
    Organizes all the .mhd headers and .raw files associated in the given baseDirectory.
    The output is an array containing objects of the type 'Mhd_Structure'.
    Optional feature: imageType to restrain the search to a certain type of image, such as 'Wild', 'Homo',..
    Optional feature: baseName to restrain the search to certain images (for example to avoid detecting .mhd results), for example 'COMSCAN'
    """
    allImages = []
    # Use findImages to get directories and image names
    allDirectories = findImages(baseDirectory)
    for dirs in allDirectories:
        # Filtering on image name
        if baseName in dirs[1] : 
            # Filtering on image type
            if imageType in dirs[0]:
                    image = Mhd_Structure.Mhd_Structure()
                    image.setStructure(dirs[0], dirs[1])
                    print( "Reading "  + image.imageName + " ..")
                    # Add result to output
                    allImages.append(image)
    return allImages

#readAllImages(rootd, imageType = "Wild" , baseName = "COMSCAN")
