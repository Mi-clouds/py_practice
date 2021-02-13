# Python delete file
# delete a file
# to delete a file you must import the OS module and run its os.remove() function
# to avoid getting an error, I can check if the file exists before I try to delete

import os
if os.path.exists("..files/file_del.txt"):
    os.remove("../files/file_del.txt")
else:
    print("The file does not exist.")

# to delete a folder, use the os.rmdir() method:
# remember I can only delete empty folders

#import os
#os.rmdir("myfolder")

import os
if os.path.exists("emptyfolder"):
    os.rmdir("emptyfolder")
else:
    print("The folder does not exist.")



