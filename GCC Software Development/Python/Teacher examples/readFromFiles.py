# We have three files, with which we have to read from and add to their
# individual lists.
# The files are;
#
# firstName.txt - which contains first names
# lastName.txt - which contains last names
# ages.txt - which contains their ages
# 
# We then want to combine the three lists into one
# and then find out the following information;
# how many people are in the combined list
# what the age of the oldest person is
# and find the average age

# Then display the results

import os
import sys
location = os.path.dirname(os.path.realpath(sys.argv[0]))

# Global Variables
firstNames = []
lastNames = []
ages = []
combinedList = []

def readFiles():
    global firstNames, lastNames, ages

    with open(os.path.join(location,"firstName.txt"), 'r') as firstname:
        firstNames = firstname.read().splitlines()

    with open(os.path.join(location,"lastName.txt"), 'r') as lastname:
        lastNames = lastname.read().splitlines()

    with open(os.path.join(location,"ages.txt"), 'r') as age:
        ages = age.read().splitlines()

def combineLists():
    global firstNames, lastNames, ages, combinedList
    combinedList = zip(firstNames, lastNames, ages)
    combinedList = list(combinedList)


def displayList(combinedList):
    for var in combinedList:
        print(f"{var[0]} {var[1]} is or was {var[2]}")

def countOccurances(combinedList):
    count = 0
    for var in combinedList:
        count += 1
    print(f"There are {count} records")

def findOldest(combinedList):
    age = 0
    varAge = 0
    for var in combinedList:
        varAge = int(var[2])
        if varAge > age:
            age = varAge
    print(f"Oldest age is {varAge}")

readFiles()
combineLists()
countOccurances(combinedList)
findOldest(combinedList)


