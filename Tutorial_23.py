


# List methods in python

ls = [2, 90, 4, 5, 6, 7, 8]
# print(ls)

##################################################

# using append() method for adding value in the end of the list

# ls.append(45)
# print(ls)


#############################################################

# using sort() method
# Sorting list in assending order

# ls.sort()
# print(ls)

#######################################################

# Sorting list in decending order

# ls.sort(reverse=True)
# print(ls)

#########################################################

# It will reverse the array

# ls.reverse()
# print(ls)

##########################################################

# This method returns the index of the first occurence of the list item 

# ls.index(90) # its not working

# print(ls.index(90))  # it works

#######################################################################

# Count method count the How many times a specific number occurs in the list


# ls = [1, 2, 354, 45645, 456, 1, 2, 65, 2, 54, 2, 43, 2, 43, 2]
# print(ls.count(2)) # it works

#######################################################################

# Creating copy of the list

# You should try to avoid these things in python
# Because it will also change the original python list
# instead of this we should use copy method

# l = [25, 20, 10, 30, 35, 50, 20]

# m = l
# m[0] = 0

# print(l)
# print(m)


#########################################################
# Using copy method
# The value of l is the orignial value but the value of m only change

# l = [26, 20, 10, 30, 35, 60, 20]

# m = l.copy()

# m[0] = 60

# print(l)
# print(m)

###################################################


# Adding value in a specific index using insert method

# l = [26, 20, 10, 30, 35, 60, 20]

# l.insert(2, 5555)

# print(l)


################################################
# Combining two lists using extend() method

# Combining m list in the end of l list

# l = [26, 20, 10, 30, 35, 60, 20]

# m = [100, 200, 300]

# l.extend(m)

# print(l)


##########################################################

# WE can combine (concatenate two list)

l = [26, 20, 10, 30, 35, 60, 20]

m = [100, 200, 300, 400]

k = l + m

print(k)








