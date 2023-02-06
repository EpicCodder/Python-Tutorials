


# Creating our first class

class Person:
    name = "Harry"   # These are properties
    age = 25
    networth = 10
    occupation = "Web Developer"


# Self means woh object jis ke liye method call kiya ja raha hai

    def info(self): # this is method
        print("The name is :", self.name, " And the occupation is : ", self.occupation)




# Creating object of the class
a = Person()

a.name = "Legends"
print(a.name)

# a.name = "Shubham"
# a.occupation = "Accountant"

# print("The name is : ",a.name, " and the occupation is : ", a.occupation)

a.info()


#################################################################
# Creating second object

b = Person()

b.name = "Suleman"
b.occupation = "Web Developer"


print("The name is : ", b.name, " and the occupation is : ", b.occupation)

