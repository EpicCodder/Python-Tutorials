



# Dictionaries in python

# Dictionary are the ordered collection of data items


# Dictionary is the collection of key value pair

# dict = {
#     "Name" : "Harry",
#     "Age" : 35,
#     "City" : "Lahore"
# }


# print(f"Hello my name is {dict['Name']}")


###############################################################

# dict = {
#     45 : "Usama",
#     46 : "Suleman",
#     47 : "Ali"
# }


# print(f"Hello my name is {dict[47]}") # using f string
# print("Hello my name is : ", dict[47]) # Without using f string


# Note : From python 3.7 to onward dictionaries are ordered 
# In previous versions dictionarires are not ordered

################################################################

# 2 methods of accessing dict values


# dict = {
#     45 : "Usama",
#     46 : "Suleman",
#     47 : "Ali"
# }


# # if we want program throw an error when we give false value 
# # we can use this method
# # It will give an error

# print(f'Hello my name is : {dict[5]}')

# # WE can use .get method
# # In this method program does not throw any error if the value is not present
# # Note : it will return None

# print(f"Hello my name is : {dict.get(5)}")



#############################################################################


# How we can access all keys of the dictionary

# dict = {
#     45 : "Usama",
#     46 : "Suleman",
#     47 : "Ali"
# }

# We use keys() method

# print(dict.keys())

# print(type(dict.keys()))


# for key in dict.keys():
#     print("The value of keys are ", key)


###################################################################

# if we want to print all values we will use .values() method

dict = {
    45 : "Usama",
    46 : "Suleman",
    47 : "Ali"
}

# print(dict.values())

# for values in dict.values():
#     print(f"The values of keys are {values}")



#########################################################################

# Next method for iterating the key

# dict = {
#     45 : "Usama",
#     46 : "Suleman",
#     47 : "Ali"
# }

# for key in dict.keys():
#     print(f"The value to the corresponding key is : {dict[key]}")


###########################################################################

# using key.items() method for displaying both key values pair


# dict = {
#     45 : "Usama",
#     46 : "Suleman",
#     47 : "Ali"
# }


# print(dict.items())


# for key, values, in dict.items():
#     print(f"The key is : {key} and the value is : {values}")



###########################################################################


# summary we use these methods

# keys() for displaying dictionary keys
# values() for displaying dictionary values
# items()  for displaying both key values of the dictionary




