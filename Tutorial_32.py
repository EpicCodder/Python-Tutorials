

# Set methods

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}


# Method for finding the union of the number 
# print(s1.union(s2))

# # But the value of s1 and s2 remains same in this case

# print(f"The value of s1 is : {s1} and the value of s2 is {s2}")

############################################################################

# But if we want to make changes in the set we can use update method


# The value of s2 place in the s1 set (This works like union but it will change the values of set1)

# s1.update(s2)

# # The values of the s1 will be changed
# print(s1)


############################################################################

# cities1 = {"Tokyo", "Madrid", "Lahore", "Delhi"}

# cities2 = {"Tokyo", "Madrid", "Lahore", "Delhi", "Kabul", "Berlin"}

# cities3 = cities1.union(cities2)

# print(cities3)

# Note :  By using update() method we can change the values 

##############################################################################

# Now using intersection

# cities1 = {"Tokyo", "Madrid", "Lahore", "Delhi"}

# cities2 = {"Tokyo", "Madrid", "Lahore", "Delhi", "Kabul", "Berlin"}

# print(cities1.intersection(cities2))
# cities3 = cities1.intersection(cities2)

# print(cities3)

################################################################################

# Now changing the values using intersection_update method

# cities1 = {"Tokyo", "Madrid", "Lahore", "Delhi"}

# cities2 = {"Tokyo", "Madrid", "Lahore",  "Kabul", "Berlin"}

# cities1.intersection_update(cities2)

# # The value of cities1 will be changed

# print(cities1)

#########################################################################

# Symmetric difference

# (A  union B) - A intersection B is the symmetric difference 
# it means all values jo common nahi hain


# The difference and difference_update() methods prints only items That are 
# only present in the original set not in both the set.

# cities1 = {"Tokyo", "Madrid", "Lahore", "Delhi", "Spain", "Cairo"}

# cities2 = {"Tokyo", "Madrid", "Lahore",  "Kabul", "Berlin"}

# cities3 = cities1.difference(cities2)
# print(cities3)


# cities1.difference_update(cities2)
# print(cities1)

###########################################################################

# isdisjoint() method checks if the items of given set are present in another set
# This method returns false if items are present . else it returns true.

############################################################################

# issuperset() 

# The issuperset() method checks if all the items of a particular set are present 
# in the original set . It returns true if all the items are present else it returns false

#############################################################################

# issubset() method

###########################################################################

# if we want to add single item to the set we can use add() method

# se = {"Hello", "World", "How", "Are", "You"}


# # Adding the single value in the set
# se.add("Kabul")

# print(se)

##############################################################################

# if you want to add() multiple values we can make another set and 
# update the values

# cities1 = {"Tokyo", "Madrid", "Lahore", "Delhi"}

# cities2 = {"Tokyo", "Madrid", "Lahore",  "Kabul", "Berlin"}

# cities1.update(cities2)

# print(cities1)


#####################################################################

# remove() / discard()

# The main difference between remove and discard is that when we remove
# something  remove() method raises an error while discard() will not


se = {"Spain", "Berlin", "Tokyo", "Madrid", "Dehli"}

print(se)

# Removing the value
# Remove will give an error when the value is not present
# se.remove("Spain")

# se.remove("japan")

# While discard not give any error

# se.discard("japan")

# print(se)

########################################################################

# pop() method

# This method remove the last element of the set but we cant catch 
# Which element is popped because the values are unordered in the set


# se = {"Spain", "Berlin", "Tokyo", "Madrid", "Dehli"}

# se.pop()

# print(se)

#########################################################################

# del keyword

# this method deletes the entire set

# se = {"Spain", "Berlin", "Tokyo", "Madrid", "Dehli"}

# del se
# # Now our se set is deleted
# print(se)

#########################################################################

# clear() method

# Clear method clears all the items in the set and points an empty set
# This will not delete the set but delete all items in the set 

# cities = {"Lahore", "Faisalab", "Multan", "Islamabad"}

# cities.clear()

# print(cities)


##########################################################################

# Check if value exist in the set or not
cities = {"Spain", "Berlin", "Tokyo", "Madrid", "Dehli"}


if "Spain" in cities:
    print("Yes it is present")
else:
    print("No it is not present")
