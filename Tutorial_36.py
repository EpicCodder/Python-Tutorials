

# Python exception handling try except


# Making the table

# But if we enter string as an input it will give an error
# by default the execution of the program is stopped when error occured
# if if we use try except we can print the error and execute the lines


# Exception handling is the process of responding to unwanted and unexpected events



# n = input("Please Enter your number : ")

# print(f"The table of {n} is ")


# try:
#     for i in range(1, 11):
#         # print(f"{n} X {i} = {n*i}")
#         print(int(n), " X ", int(i) ," = ", int(n) * int(i))
# except Exception as e:
#     print(e)


# print("Some important lines of code")
# print("The end of the program")


################################################################

# We can also print our own lines in except 

# n = input("Please Enter your number : ")

# print(f"The table of {n} is ")


# try:
#     for i in range(1, 11):
#         # print(f"{n} X {i} = {n*i}")
#         print(int(n), " X ", int(i) ," = ", int(n) * int(i))

# # Just using except keyword
# except:
#     print("Invalid type of input")


# print("Some important lines of code")
# print("The end of the program")


#############################################################################

try:
    num = int(input("Please Enter your number : "))
    a = [6, 5]
    print(a[num])
    
except ValueError:
    print("Number entered is not an integer")

# ik line mein 5 types ke error bhi a sakty hain

except IndexError:
    print("Index Error")






