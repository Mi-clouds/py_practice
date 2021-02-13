# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files

# File handling
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename and mode
# These are four different methods (modes) for opening a file:

# 'r' = read = default value. Opens a file for reading, error if the file does not exist
# 'a' = append = opens a file for appending, creates the file if it does not exist
# 'w' = write = opens a file for writing, creates the file the file if it does not exist
# 'x' create - creates the specified file, return an error if the file already exists

# In addition you can speicify if the file should be handled as binary or text mode.
# 't' - text ' default mode, text mode
# 'b' - binary = binary mode (e.g. images)

# Syntax - to open a file for reading it is enough to specifiy the name of the file:
# f = open("demofile.txt")
# The code above is the same as:
# f = open("demofile.txt", "rt")

# the file must exist or you will get an error
# Open a file on the server
# Assume we have the following file, located in the same folder as Python:
# demofile.txt
# To open the file, use the built-in open() function
# The open() returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt", "r")
print(f.read())

f = open("../files/paradise.txt", "r")
print(f.read())
f.close()

# read only parts of a file
# by default the read() method returns the whole text, but you can also specify how many characters you want to return
f = open("../files/smooth_criminal.txt", "r")
print(f.read(20))

# read lines
# read one line of the file

f = open("../files/smooth_criminal.txt", "r")
print(f.readline())
print(f.readline())

# The new line character in files
# The new line character \n is also found in files, but it is "hidden".
# When you see a new line in a text file, a new line character has been inserted.
with open("../files/smooth_criminal.txt", "r") as f:
    print(f.readlines())
f.close()

# by looping through the lines of the file, you can read the whole file, line by line
f= open("demofile.txt", "r")
for x in f:
    print(x)

# close files - best practice
# it is a good practice to always close the file when you are done with it
# I should always close my files, in some cases, due to buffering, changes made to a file may not show until I close the file.
f = open("demofile.txt", "r")
print(f.readline())
f.close()
