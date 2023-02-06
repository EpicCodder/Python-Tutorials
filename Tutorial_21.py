


# Arguments in python

# Diffference between parameters and arguments

# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that are sent to the function when it is called.

############################################################

# def average(a, b):
#     print("The average is : ", (a+b)/2)

# average(10, 20)

############################################################

# Getting input from the user

# fname = input("PLease Enter your first name : ")
# lname = input("Please Enter your last Name : ")


# parameters f and l (according to my information)

# def flname(f, l):
#     print("Hello ", f, l, " How are you!" )


# flname(fname, lname)


#############################################################

#Key word arguments
# if you follow this style you dont need to follow the order

# def average(a=5, b=10):
#     print("The average is ", (a+b)/2)


# average(b=20, a=30)


##############################################################

# The by default value of b is : 4

# def average(a, b=4):
#     print("The average of the numbers are : ", (a+b)/2)


# average(10)


###############################################################

# Giving multiple values to the function
# yeh value as a tuple le ga

# def average(*number):
#     sum = 0
#     print(type(number))

#     for i in number:
#         sum = sum + i
    

#     print("The average of the numbers are : ", sum/len(number))



# average(10, 20, 30, 40, 50)


#####################################################################

# Giving multiple values in a key value pair



# def name(**name):
#     print(type(name))
#     print("Hello ", name["fname"], name["lname"], "How are you")


# name(fname = "Muhammad", lname = "Usama")


########################################################################

# I want to return value instead of printing value

# def average(*number):
#     sum = 0

#     for i in number:
#         sum = sum + i 
    
#     return sum/len(number)

# # I store the value of average in c variable

# c = average(10, 20, 30, 40)

# print("The average of the numbers are : ", c)


###################################################################

#



