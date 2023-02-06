

import time

timestamp = time.strftime('%H:%M:%S')

hours = int(time.strftime("%H"))


print(timestamp)
print(hours)

hours = int(input("Please Enter your nunber : "))

if(hours >0 and hours < 12):
    print("Good Morning")
elif(hours >=12 and hours <=19):
    print("Good Eening")
else:
    print("Good Night") 

