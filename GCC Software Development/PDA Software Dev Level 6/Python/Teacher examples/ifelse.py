# Author - Paul Dorman
# Date - 12/12/23
# Description - If - elif - else

def EnterScore():
    # Input: Get the numeric score from the user
    score = int(input("Enter the score: "))

    # Determine the grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # Output: Print the grade
    print("The grade is:", grade)

def OddEven():
    # Input: Get an integer from the user
    number = int(input("Enter an integer: "))

    # Check if the number is odd or even
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")



