#!/usr/bin/python


"""

A file with a name like picture.jpg is said to have an extension of "jpg"; i.e. the extension of a file is the 
part of the file after the final period in its name. Write a program that takes as an argument the name of a 
directory (folder) and then finds the extension of each file. Then, for each extension found, it prints the number 
of files with that extension and the minimum, average, and maximum size for files with that extension in 
the selected directory. 

"""

import os
import pprint
total = 0

# add file read input stuff here

ext_dict = {}

for root, dirs, files in  os.walk('IMAGES'):
    for singlefile in files:
        if not ext_dict.get(singlefile[-4:]): #if ext is not in the dict, add it
            ext_dict[singlefile[-4:]] = []
        ext_dict[(singlefile[-4:])] += [(singlefile, os.path.getsize(os.path.join(root, singlefile)))]

             


pprint.pprint(ext_dict)



        #if os.path.getsize(os.path.join(root, singlefile)) > 0:
            # total += 1
            #print singlefile, os.path.getsize(os.path.join(root, singlefile))