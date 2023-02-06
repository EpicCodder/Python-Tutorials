


# Access Specifier

# Python mein public private protected name ki koi cheez nai hoti

# Access modifiers in python programming are used to limit the access 
# of the class

# class Employee:
#     def __init__(self, a):
#         self.name = a
    

# a = Employee("Legends")

# print(a.name)

# Any instance variable of the class followed by the self keyword
# are publicly Accessable


##############################################################################

# But agar hum __ underscore use karein self ke baad to woh private ho jaiga
# aur hum usse access nai kar painge . We can access but not in the normal way


# class Employee:
#     def __init__(self, a):
#         self.__name = a   # We cannot access it directly
    


# a = Employee("Legends")



# print(a.name) # Cannot be accessed directly in this way

# # But we can access it in this way

# print("Hello my name is : ", a.__name)


###############################################################################

# Today work

# class Employee:
#     emp1 = 20  # Same work 


# a = Employee

# # a.emp1 = 20 # Same work
# # By default variable accessable outside the class in python
# # all methods and variables in python are by default public


# print(a.emp1)


#####################################################################

# class Employee:
#     def __init__(self, age, id):
#         self.name = "Hello world"
#         self.age = age
#         # Now we make a private variable using double underscore __id
#         # we cannot access this variable directly

#         # But we can access it using class name then attribute name
#         self.__id = id



# a = Employee(45, 101)
# print(a.name)

################################################################################

# print(f"The age of the student is : {a.age}")

# Now we are accessing private variable
# This is also called name mangling


###############################################################################
###########################################################################3###











# print("This is the private variable value : ", a._Employee__id)


#############################################################################

# What is name mangling

# In python name mangling is a technique used to protect class private 
# and super-class private attributes from being accidently overwritten


#######################################################################

# if we want to see which methods and attributes we use in this class
# we can use a.__dir__() method

# print(a.__dir__())


#######################################################################

# Protected methods and properties of the class

class Student:
    def __init__(self):
        self._name = "Harry"
    

    def _funName(self):
        return "Code with harry"
    


class Subject(Student):
    pass


obj = Student()
obj1 = Subject() 

# print(obj._name) # WE can access it
# print(obj._funName()) # We can also access it

# print("Below we are inheritance concept class")
# print(obj1._name)
# print(obj1._funName())


#####################################################

# Now i am printing the availabe methods, attributes and class

print(obj.__dir__())
print(30 * "#")

print(obj1.__dir__())