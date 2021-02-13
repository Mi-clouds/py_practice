# write to an existing file
# to write an existing file, you must add a paramenter to the open() functions:
# "a"  - append - will append to the end of the file
# "w" - write - will overwrite any existing comments

# open the file and append the content to the file:
f = open("../files/demo_text2.txt", "a")
f.write("Now the file has even more and more and more content!")
f.close()

#open and read the file after the appending:
f = open("../files/demo_text2.txt", "r")
print(f.read())

# open the file "demofile3.txt" and overwrite the content
f = open("../files/demo_file3.txt", "w")
f.write("Whoops! I have deleted the content!")
f.close()

# open and read the file after appending:
f = open("../files/demo_file3.txt", "r")
print(f.read())
f.close()





