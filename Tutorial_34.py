

# Dictionary Method

# Employee performance

# ep = {
#     122 : 45, 
#     123 : 89,
#     124 : 90,
#     125 : 44,
# }

# ep2 = {
#     222 : 56,
#     223 : 70,
#     234 : 20
# }

# # Now we will combine two dictionary

# ep.update(ep2)

# for key, value in ep.items():
#     print(f"The key is : {key} and the value is : {value}")


##########################################################################

# Using clear() method for clearing the key values of dictionary

# ep = {
#     122 : 45, 
#     123 : 89,
#     124 : 90,
#     125 : 44,
# }

# print(ep)

# for key, values in ep.items():
#     print(f"The keys are : {key} and the values are : {values}")


# Now i am clearing the dictionary

# ep.clear()

# print(ep)

####################################################################

# Making an empty dictionary

# emp = {}
# print("This dictionary is empty : ", emp)


####################################################################

# popping the value from the dictionary


# ep = {
#     122 : 45, 
#     123 : 89,
#     124 : 90,
#     125 : 44,
# }


# print(ep)

# Pop the key and value pair of 123

# ep.pop(124)
# print(ep)

#############################################################

# Method popitems() remove the last key value pair of the dictionary


ep = {
    122 : 45, 
    123 : 89,
    124 : 90,
    125 : 44,
}

ep.popitem()

print(ep)


#########################################################################

# if we want to remove the dictionary we use del keyword


# ep = {
#     122 : 45, 
#     123 : 89,
#     124 : 90,
#     125 : 44,
# }


# This we delete the dictionary
# del ep

# print(ep)

###################################################################

ep = {
    122 : 45, 
    123 : 89,
    124 : 90,
    125 : 44,
}

print(ep)

del ep[124]

print(ep)


# We can also check the python dictionary documentation


