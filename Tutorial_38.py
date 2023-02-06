



# Raising custome error

# In python we can raise the custom error by using the raise keyword


# a = int(input("PLease Enter the number in between 5 to 9 : "))



#this will raise the error if you entere the value smaller than 5 and greater than 9 

# if(a<=5 or a>=9):
#     raise ValueError("Value should be between 5  to 9")


# WE can search (Python error classes)
# In this way we can find list of built in exceptional classes


###########################################################################

# Defining custom exceptions

# We can also define custome exceptions

##########################################################################

# Quiz

str = input("Please Enter the quit in small laters : ")


if(str == "quit"):
    pass
else:
    raise ValueError("You entered the wrong input")

