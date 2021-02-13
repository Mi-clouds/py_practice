import sys, glob, os
print(sys.argv)
#prints the name of the file I am editing now
# os module allows us to interact with the underlying operating system in several different ways
# e.g. navigate the system, get file information, look up and change environment, variables, move files around
# to see all the attributes in the OS module print directory of os
print(dir(os))

print(os.getcwd())
# get current working directory
# change working directory with chdir
os.chdir("C:/Repositories")
#
#print(os.getcwd())
#print(os.listdir())

#os.rmdir("filepath")
#os.removedirs("filepathname")
# removes folder/s better to use rmdir to removed specific folders

# os.rename("original name", "new name")
# rename file or folder

# os.stat("demofile.txt")
# print out details of a file
# os.stat("filename.txt").st_size)
# os.stat("filename.txt").st_mtime)
# from datetime import datetime (add this at the top under import os
#mod_time = os.stat("demo.text).st_mtime
print(datetime.fromttimestamp(mod_time))

# walk method
# generates 3 values it yeilds direcotry paths, directories within those paths and the files within those paths
from dirpath, dirnames, filenames in os.walk("filepath")
    print("curret path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print()
# starts top down by default


# print list of files in current directory or pass a file path to a new directory
# sys short for system - used for command line arguments
print(sys.version_info)
# make a new folder/s makedir will make a series of subfolders if needed - better to us makedirs

# os.environ.get("HOME")
# user home directory path
#do not concatenate this with file names - often goes wrong

#reading and writing paths to different paths for files
#os.path.join(os.environ.get("HOME"), "test.txt")

# with open(file_path, "w") as f:
#    f.write

# os.path.basename("filname of path we are working on /tmp/test.txt")
# os.path.dirname("Filename")
# os.path.spltip("tmp/test,txt)")
# os.path.exists("tmp/tst.txt")
# os,path.isdir("tmp/tst.txt") # Returns True or False
# os,path.isfile("tmp/tst.txt") # Returns True or False
# os,path.splitxt("tmp/tst.txt") # returns file path and file separately - easier than string splicing

os.mkdir("os-dmo-2")
os.makedirs("os-demo-2")
# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
for name in glob.glob(pattern):
    print(name)

# TODO: use os.path.getsize to find each file's size
size = os.path.getsize(pattern)
print("Size (in bytes) of '%s':" %pattern, size)
# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
