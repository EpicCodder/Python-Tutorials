

# methods of tuple



# WE cannot manuplate the tuple not in direct way
# if you want to change add remove and delete tuple items
# then first you must convert the tuple to a list


# countries = ("Spain", "Italy", "India", "england", "Germany")

# print(countries)

# temp = list(countries)
# temp.append("Russia")

# # For Removing value using index

# # temp.pop(2)

# print(temp)
# temp[2] = "Ukrain"
# print(temp)

# countries = tuple(temp)
# print(countries)


# Conclusion : in this way we can change the values of tuples indirectly
# not directly

############################################################################

# We can concatinate two tuples and make new one

# countries = ("Pakistan", "Afghanistan", "Bangladaish", "India")
# countries2 = ("Vietnam", "China", "Korea")
# southEastAsia = countries + countries2

# print(southEastAsia)
# print("The data type is : ", type(southEastAsia))

############################################################################

tup = (0, 1, 2, 3, 2, 5, 2, 5, 2, 3, 5, 3, 6)

res = tup.count(2)
print("The number 2 is : ", res, "times in tuple")


res = tup.index(6)
print("The index of the given number is : ", res)


# using more values of index

# Finding value=2 ,Starting index 3 ending index 5

res = tup.index(2 ,3, 5)
print(res)







