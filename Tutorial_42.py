



 # Python enumerate function

# lis = [10, 20, 30, 40, 50, 60, 70, 80, 90]


# for index, value in enumerate(lis):
#     print("The index of the value is : ", index, "and the value is : ", value)


# for index, value in enumerate(lis):
#     if index == 4:
#         print("You have reached at index 4 :", value)
#     else:
#         print("The index of the value is : ", index, "and the value of the index is : ", value)


########################################################################################


# Now we will check the type of index and value

# lis = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# for index, value in enumerate(lis):
#     if index == 4:
#         print("You have reached at index 4 :", value)
#     else:
#         print("The index of the value is : ", index, "and the value of the index is : ", value)



############################################################################

# We can also start the indexing from the specifi value


lis = [10, 20, 30, 40, 50, 60, 70, 80, 90]


# The index starts from 5 

for index, value in enumerate(lis, start=5):
    print(f"The index is {index} and the value is {value}")
