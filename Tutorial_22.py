
# Tutorial List


######################################
# Making list
# marks = [22, 55, 66, 77, 88]


#################################################3
# Printing the value of list using index

# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])


#############################################################
# Iterate the list


# marks = [22, 55, 66, 77, 88, 100, 345, 346,45, 6,4, 576,56, 7,56, 7,567,56,756]

# for i in marks:
#     # print(i, end=" ")
#     print(i,end=" ")


################################################################

# We can store multiple type of data in list

# list1 = [3, 54, "Fname", "lname", 45.33]
# print(list1)

##############################################################

# Printing negative index from the list


# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print(len(list1))

# print(list1[-3]) #Negative indexing

# # Negative indexing technique

# print(list1[len(list1) -3])

# it is a good practice to convert negative index into positive 
# than it will be easy to work with


####################################################################

# How to find a specific word in the list

# list1 = [10, 20, 30, "Harry", "Pytho", "Geeks"]

# if "Pytho" in list1:
#     print("Yes it is present")
# else:
#     print("No it is not present")


#######################################################################


# Finding the value from the String 
######## it is so easy we dont need to use for loop for this


# str1 = "Helloworldhowareyou"

# if "z" in str1:
#     print("Yes it is present")
# else:
#     print("No it is not")


######################################################################

# Finding the word from the word

# if "olo" in "yolo":
#     print("Yes it is ")
# else:
#     print("No it is not")

#######################################################################

# List slicing

# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print(list1[:]) # it starts from 0 and end at len(list1)-1
# print(list1[0:len(list1)])
# print(list1[2:4])
# print(list1[1:]) # starting from 1 and ending at len(list1)-1

#####################################################################

# jump index is use for jump from in the value in a specific order


list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print(list1[0:len(list1):2])
# print(list1[::2])
# print(list1[:6: 2])
# print(list1[:len(list1)])  # 1 to len(list1)
# print(list1[2:])



# print(list1[0:len(list1)]) # it prints all the list
# print(list1[::]) # it all prints all the list

# print(list1[0: len(list1)-1]) # Both are the same
# print(list1[0:-1])  # Both are the same

######################################################################

# Jump index is use for jump from a value is a specific order

# print(list1[::2]) # both are same
# print(list1[0:len(list1):2]) # both are same


#######################################################################

# What is list comprehension
#list comprehension means we are generating list on the fly


# lis = [i for i in range(20)]
# print(lis)

# lis = [o*2 for o in range(10)]
# print(lis)

#####################################################################

lis = [i for i in range(20) if i%2==0]
print(lis)





















