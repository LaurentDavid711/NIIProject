# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 14:30:25 2016

@author: L.David
"""
import mhd_utils
import os

class Mhd_Structure:
    """
    A class that organizes the information on a given raw image and its associated .mhd header.
    An object of type Mhd_Structure contains:
    - the image name
    - its path
    - optionnally a type (Wild, Homo,..)
    - a dictionnary containing the information from the .mhd header
    - an array containing the image volume
    This class relies on the mhd_utils functions to read .mhd files.
    """

    def __init__(self):
        self.imageName = ""
        self.directory = ""
        self.imageType = ""
        self.header = {}
        self.volume = []
        
    def setStructure(self, directory, imageName):
        """
        sets the attributes, given the image name and its path (directory).
        """
        self.directory = directory
        # sets the image type, if the information is available, ie in the image folder's name 
        if "Wild" in directory:
            self.imageType = "Wild"
        elif "Homo" in directory:
            self.imageType = "Homo"
        elif "Hetero" in directory:
            self.imageType = "Hetero"
        else:
            self.imageType = "None"
            
        self.imageName = imageName
        baseDirectory = os.getcwd()
        # Change directory to access the image
        os.chdir(directory)
        # retrieves volume and header information from the mhd_utils function
        self.volume, self.header = mhd_utils.load_raw_data_with_mhd(imageName)
        os.chdir(baseDirectory)
        return
        
    def setImageType(self, typeName):
        """
        Sets the image type manually
        """
        self.imageType = typeName
        
    def getStructure(self):
        return self.imageName, self.directory, self.imageType, self.header, self.volume

