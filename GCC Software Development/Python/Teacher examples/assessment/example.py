# Author : Paul Dorman
# Description : Read and Process 3 files
# Date : 13th Feb 2024

# Use libraries to find working directory
# and to change path
import os
import sys
location = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(location)

# Function to read the individual files
def readFiles():
    # read manufacturer.txt into mList
    with open("manufacturer.txt", 'r') as filename:
        mList = filename.read().splitlines()

    # read cache.txt into cList
    with open("cache.txt", 'r') as filename:
        cList = filename.read().splitlines()     

    # read processor.txt into pList
    with open("processor.txt", 'r') as filename:
        pList = filename.read().splitlines()    

    # combine all three list into combinedList and convert to list
    combinedList = list(zip(mList, pList, cList))
    for item in combinedList:
        print(item)

    return combinedList

# Process List to find
# number of items in list
# the quickest pc
def processList(combinedList):
    countItem = 0
    fastestPC = 0
    name = ""
    for item in combinedList:
        countItem += 1
        speed = calculateSpeed(item[1], item[2])
        if speed > fastestPC:
            fastestPC = speed
            name = item[0]
    print(f"{name} has the fastest speed of {fastestPC}")
    print(f"There are {countItem}'s")

def calculateSpeed(processor, cache):
    speed = float(processor) * float(cache)
    return speed


combinedList = readFiles()
processList(combinedList)
