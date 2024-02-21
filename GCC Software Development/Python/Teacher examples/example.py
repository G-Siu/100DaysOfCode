# Author - Paul Dorman
# Date - 23rd Jan 2024
# Description - Darts Scoring App

# Load the libray os that provides operating system functions
import os

# Call the os function system to clear the screen
os.system('cls')

# This function asks user to enter the mark of the first dart
# Also validate to make sure the number falls between 0 and 60
# Returns the value of the first dart
def GetFirstDart():
    firstdart = -1
    while firstdart < 0 or firstdart > 60 :
        firstdart = int(input("Please enter score of first dart : "))
    return firstdart

# This function asks user to enter the mark of the second dart
# Also validate to make sure the number falls between 0 and 60
# Returns the value of the second dart
def GetSecondDart():
    seconddart = -1
    while seconddart < 0 or seconddart > 60 :
        seconddart = int(input("Please enter score of second dart : "))
    return seconddart

# This function asks user to enter the mark of the third dart
# Also validate to make sure the number falls between 0 and 60
# Returns the value of the third dart
def GetThirdDart():
    thirddart = -1
    while thirddart < 0 or thirddart > 60 :
        thirddart = int(input("Please enter score of third dart : "))
    return thirddart

# This functions receives the three scores and calculates the total score
# Returns the total score
def CalculateScore(first, second, third):
    score = first + second + third
    return score

# This functions receives the total score and grades it
# prints and grades score
def GradeScore(score):
    if score >= 100:
        print(f"Excellent score of {score}")
    elif score >= 60:
        print(f"Average score of {score}")
    else:
        print(f"That's a poor score of {score}")

# Call GetFirstDart() function and returns value to firstDart
firstDart = GetFirstDart()
# Call GetSecondDart() function and returns value to secondDart
secondDart = GetSecondDart()
# Call GetThirdDart() function and returns value to thirdDart
thirdDart = GetThirdDart()

# Calls the CalculateScore() function and passes the three variables;
# firstDart, secondDart and thirdDart
# It then calculates the total score and returns the value to score
score = CalculateScore(firstDart, secondDart,thirdDart)

# This passes the score to the GradeScore functions that then
# grades and prints the score
GradeScore(score)
