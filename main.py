# Inspiration from https://www.includehelp.com/python/copy-and-replace-files-in-python.aspx

# importing the modules
import os
import shutil

# getting the current working directory
src_dir = os.getcwd()

# printing current directory
print(src_dir) 

# copying the files
shutil.copyfile('test.txt', 'test.txt.copy2') #copy src to dst

# printing the list of new files
print(os.listdir()) 