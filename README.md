# Read and Write raw files and associated .mhd headers in python.
The goal of this repository is to make reading raw images and .mhd headers easier. 
Given a path, the script will find all the raw .mhd files in the folders and sub-folders.
For every image, an object will be created, containing the following information:
- the image path
- the image name
- a dictionnary containing the .mhd header information
- an array containing the raw image volume
- optionally the image type can be added.

This repository contains four files:
- readMhdImages which is the entry point of the program and has basic input functions to choose which folder to scan
- Mhd_Structure which is a class to build mhd object given the image's path
- mhd_browse which contains function to look for mhd files in all the folders
- mhd_utils which contains functions to read and write .mhd files in python (from https://github.com/yanlend/mhd_utils)

The idea for the repository is to make accessing to medical images easier, to be able to process/normalize/register them afterwards.
