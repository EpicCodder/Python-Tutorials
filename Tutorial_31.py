

# Set in python

# By the book definition

# set is a collection of wel defined object

# Note : Set mein repeated values nahi hotin

# Sets are unordered collection of data items.
# Sets are unchangable means you cannot change the
# items of the set once you created. Sets do not contain duplicate items
# The values of the set cannot be accessed using index number
# set order maintain nai karta (random values print hongi jo set mein hain)


#####################################################################

s = {2, 5, 6, 2, 5, 8, 9, 10}

# Repeated values print nahin huwin
# print(s)

####################################################################

# Sets also contain different types of values

# se = {False, 1.55, 45, "Legends"}

# print(se)

# print(type(se))

# WE cannot access the value of a set using index
# print(se[1]) 

####################################################################

# Quiz try to create an empty set . Check using the type function wheather
# The type of your variable is a set.

# harry = {}   # in this way we made empyt dictionary not an empty set (wrong way for making empty dictionary)


# print(type(harry))

######################################################################

# Right way of making empty set is this

# s = set() # in this way

# print(type(s))


######################################################################

# set order maintain nai karta

# info = {"Carla", 19, False, 5.9, 19}

# # Random values print hongi jo set mein hain
# print(info)


######################################################################

info = {"Carla", 19, False, 5.9, 19, "Legends", 55}


#######################################################################

# How to access set items 
# we can access seg items using for in loop
# We cannot access the value of the set using index because 
# set do not maintain the order 


for values in info:
    print(values)
