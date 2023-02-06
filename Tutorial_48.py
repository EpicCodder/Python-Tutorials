

# Local and global scope

# x = 4

# print("The value of x outside the function Global variable : ", x)


# def hello():
#     x = 6
#     print("The value of x inside the function local variable : ", x)
#     print("Hello world")


# hello()

# print("Again The value of x outside the function global variable : ", x)


#############################################################################

# We can use global keyword inside the function and change the value of the 
# Global variable inside the function otherwise its not possible to change 
# The value of the global variable inside the function


x = 25

def my_func():
    global x     
    x = 30
    print("The value of the x inside the function is : ", x)


my_func()

print("The value of the x outside the function is : ", x)
