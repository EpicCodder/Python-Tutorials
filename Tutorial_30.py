

####################### Recursion #################################

# What is Recurssion

# Calling the function inside the function

# factorial(7) = 7 * 6*5*4*3*2*1

# factorial(0) = 1


#########################################################################

# Writing program for finding fibonnai sequence


def fact(n):
    if( n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)


print("The factorial of this number is : ",fact(5))


############################################################

# Finding the factorial of a number

# Quiz for finding the factorial of a number


    
    