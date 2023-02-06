

# Create a programm capable of displaying questions to the user
# like kbc  
# use list data type to store the questions and their correct answers
# Displaying the final amount the person is taking home after playing the game



questions = ["Is Python is the best language in the world : ", "DSA Stands for : ", "Oop stands for : "]

answer = ["yes", "data structure and algorithm", "object oriented programming"]

num = 0

for index, value in enumerate(questions):
    print(value, end= " ")
    ans = input("")

    if(ans == answer[index]):
        print("Congradulations!  Your Answer is correction")
        num +=10
    else:
        print("Sorry your answer is not correct")


print("Your total score is : ", num , "out of ", (len(questions) * 10))