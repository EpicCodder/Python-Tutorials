

# Python file handling

# it can be text file binary file etc


#################################################################

# How to open the file in python
# Modes in python
# r for reading
# w for writing
# a for appending

# File is not avaiable so it will give an error
f = open("myfile.txt", "r")

# So now i will make file whose name is "myfile.txt"
# NOw i will print the file

print(f)

###################################################################

# How we can read the file so we will use read() method

text = f.read()

print(text)
f.close   # Now we close this file



