
# Inheritance in python


class Employee:
    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id


    
    # Method of the class
    def showDetails(self):
        print(f"The name of the employee is : {self.name} and the id is : {self.id}")


# Inherit the class Employee to the programmer
class Programmer(Employee):
    
    def defaultLanguage(self):
        print("The Default language is Python")


# Usama and 302 ye constructor mein jaingi
e1 = Employee("Usama", 302)
e1.showDetails()

e2 = Employee("Legends", 402)
e2.showDetails()


# This will give an error becuase employee class does not have any
# defaultlanguage method

# e2.defaultLanguage()

# But what if we call porgrammer class


print("#################################################################")

e3 = Programmer("Suleman", 440)
e3.defaultLanguage()
e3.showDetails()



# Types of Inheritance

# Single Inheritance
# Multiple Inheritance
# Multi level Inheritance
# Herarichal Inheritance
# Hybrid Inheritance
