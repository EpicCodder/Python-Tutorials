

# Static methods in python


# I dont understand these lines
#-----------------------------------------------------------------------
# Static methods are those methods that does not belongs to class
# and also does not belong to variable

# Static method mein hamein class ke instance ki zaroorat nai hoti
#------------------------------------------------------------------------

# WE can access the static method using the class name or oject name


# class Math:
#     def __init__(self, num):
#         self.num = num
    

#     def addtonum(self, n):
#         self.num = self.num + n
    

    
#     @staticmethod
#     def add(a, b):
#         return a + b
    

##########################################################################


# a = Math(5)

# print(a.num)
# a.addtonum(6)
# print(a.num)


##########################################################################

# WE can call the static method using the object of the class

# print(a.add(10, 20))

# # We can also call the static method using class name

# print(Math.add(40,50))

