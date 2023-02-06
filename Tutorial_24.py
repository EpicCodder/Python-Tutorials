


# Tuple data type
# Tuple are immutable the value of tuple cannot be changed



# tup = (1, 2, 3, 4, 5, 6, )
# print(tup, " and the type is : ", type(tup))

#####################################################3
# but if we give only one value


# in this way python  will confuse so
# Remember : agar hum single value ka tuple banatay hain
# to , end par lagana zaroori hai
# tup = (10)

# print("The value is : ", tup, " And the data type is : ", type(tup))

##########################################################

# tup = (10,)
# print("The value of tuple is : ", tup, " and the type is : ", type(tup))

###########################################################

# We can do positive indexing and negative indexing of tuple same like list
# This is also a tuple slicing

# tup = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# print(tup[0:5])
# print(tup[0::2])
# print(tup[0:-1])
# print(tup[1:8:2])

# print(tup[0:len(tup)])

################################################################
# We can also check the value in the tuple

# tup = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# if 60 in tup:
#     print("Yes it is present")
# else : 
#     print("No it is not present")

#################################################################


# tup = (10, 20, 30, 40, 50, 60, 70)
# print(tup)

# tup2 = tup[1:4]
# print(tup2)

#################################################################

# using count() method
# some methods of list are also working on tuple

tup = (10, 20, 30, 40, 50, 60, 70, 80, 2, 54, 2, 43, 2, 354, 2)
print(tup.count(2))

#


