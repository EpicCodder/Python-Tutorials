

class Person:

    # This is a constructor
    # Constructor is always invoked when we make object
    # we use init Method for making constructor
    # Constructor is a special method in a class 
    # used to create and initialize an object of the class

    # Constructor always return none value

    # Two types of constructors
    # parameterize constructors (jis mein hum parameters dete hain)
    # Default constructor jo ke sirf self argument leta hai

    




    def __init__(self, n, o):
        print("Hello i am a person")

        self.name = n 
        self.occup = o
            


    def info(self):
        print("The name is : ", self.name, "And the job role is : ", self.occupation)



a = Person("Usama", "Web Developer")
b = Person("Suleman", "Software Developer")

print(a.info)
print(b.info)

