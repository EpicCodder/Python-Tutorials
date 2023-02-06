


# What is the difference between instance variable and the class variables

class Employee:

    # This is same for all the Employees

    companyName = "Apple"  # This is a class variable
    noOfEmployee = 0 

    # If we want whenever the employee add the number of employee
    # will be increment



    def __init__(self, name):
        self.name = name  # These are the instance variable
        self.raise_amount = 0.02
        Employee.noOfEmployee += 1

        
    

    def showDetails(self):
        print("The name of the Employee is : ", self.name, "\nThe raise amount is : ", self.raise_amount, "\nThe Company name of the Employee is : ", self.companyName,
         "The size of the company consists of ",self.noOfEmployee,"\n##################################################################")
    



emp1 = Employee("Harry")
emp2 = Employee("Legends")


# emp1.showDetails() # Both works same
# # Employee.showDetails(emp1) # Both works same

# emp2.showDetails()
# Employee.showDetails(emp2)


############################################################################33

# If we want to change the raise amount of the emp1 we can change also change 
# it in this way


# emp1.raise_amount = 0.05
# emp1.companyName = "Pak Apple"
# emp1.showDetails()
# # The value will be Pak Apple for emp1 but not for emp2

# emp2.showDetails()

# WE can also change the name of the company in this way

Employee.companyName = "Google"

emp1.showDetails()
emp2.showDetails()

# If they find instance variable then to woh instance variable print karry ga
# otherwise yeh class variable print karry ga.











