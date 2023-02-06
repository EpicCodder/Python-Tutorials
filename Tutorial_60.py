


# Getter and setter in python OOP

# Incomplete



# Python Getter and setter

class MyClass:
    def __init__(self, value):
        self._value = value 


    def show(self):
        print(f"The value is {self._value}")


    
    # This is a geater
    @property
    def ten_value(self):
        return 10 * self._value


    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10


# Creating an object

obj = MyClass(10)

# But what if we print obj._value

obj.show()

print(obj._value)
# obj.show()