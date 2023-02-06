

# Decorators in python
# Decorators modify the functions


# Closure : Function inside a function is called closure
# Composition : Function as an argument 



def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")

    return mfx()


@greet
def hello():
    print("Legends never die")


# greet(hello)


# Continue from 7. 56 seconds






