# Author : Paul Dorman
# Description : Read and Process 3 files
# Date : 13th Feb 2024

# Use libraries to find working directory
# and to change path
import os
import sys
location = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(location)
os.system('cls')

# Function to read the individual files
def readFiles():
    # read names.txt into names list
    with open("names.txt", 'r') as filename:
        names = filename.read().splitlines()

    # read semester1.txt into s1 List
    with open("semester1.txt", 'r') as filename:
        s1 = filename.read().splitlines()     

    # read semester2.txt into s2 List
    with open("semester2.txt", 'r') as filename:
        s2 = filename.read().splitlines()   

    # read semester3.txt into s3 List
    with open("semester1.txt", 'r') as filename:
        s3 = filename.read().splitlines()              

    # combine all four lists into combinedList and convert to list
    combinedList = list(zip(names, s1, s2, s3))

    return combinedList

def calculateOverallPercentage(s1, s2, s3):
    pc = (float(s1) + float(s2) + float(s3)) / 3
    return pc

def calculateGrade(pc):
    grade = ""
    if pc >= 70:
        grade = "A"
    elif pc >= 60:
        grade = "B"
    elif pc >= 50:
        grade = "C"
    else:
        grade = "Fail"
    return grade

def displayResults(combinedList):
    countA = 0
    findHighestPC = 0
    for mark in combinedList:
        pc = calculateOverallPercentage(mark[1], mark[2], mark[3])
        grade = calculateGrade(pc)
        if grade == "A":
            countA += 1
        if pc > findHighestPC:
            findHighestPC = pc
    print(f"The number of A is {countA}")
    print(f"The highest percentage is {findHighestPC:.2f}")

combinedList = readFiles()
displayResults(combinedList)