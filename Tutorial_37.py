

# try:
#     a = [10, 20, 30, 40]
#     i = int(input("Please Enter your input : "))
#     print(a[i])
# except:
#     print("Some Error Ocurs")
# finally:
#     print("I am alwasy execut")


# Some people think why we need to use finally keyword because 
# we can use print("") statement that is always executed




############################################################################

# But what if we use try except in function Example below


def func2():
    try:
        l = [10, 20, 30, 40]
        i = int(input("Please Enter your number : "))
        a = l[i]
        return 1

    except:
        print("Some Error occurs")
        return 0
    
    # in this case print statement will not execute 
    # So thats why in this place we can use finally keyword

    # print("Legends never die")

    # Now finaly keyword will executed
    finally:
        print("This line is always executed")


x = func2()

print(x)