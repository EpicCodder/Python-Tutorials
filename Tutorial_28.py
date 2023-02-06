

# F string in python is used for string formatting


###############################################################################

# .format() method is not so convinient so thats why we use string formating

# letter = "Hello my Name is {} and i am from {}"

# name = "Harry"
# country = "Pakistan"



# # .format() is a string method
# print(letter.format(name, country))


##########################################################################

# We can also give indexing or numbering if we give the value in random order


# letter = "Hello my Name is {1} and i am from {0}"
# name = "Harry"
# country = "Pakistan"


# # .format() is a string method
# print(letter.format(country, name))


###########################################################################

# python 3.6 or above mein introduce kiya gaya hai

# Now using f string

name = "Harry"
country = "Pakistan"


print(f"Hello my name is {name} and i live in {country}")

#####################################################################

# .2f in f string

price = 233.54324

# is tarhan yeh just 2 values print karry ga after the decimal number
print(f"The price of the meal is {price:.2f}")


##################################################################

# We can also multiply the value but the value type will be string

print(f"The sum is {20 + 40}")

print(type(f"{30 *4}"))


#################################################################

# If we want to display curly brackets as it is to hummein 
# double curly brackets use karna parienge

print(f"Hello my \"name\" is {name} and i live in {{country}}")


##################################################################


