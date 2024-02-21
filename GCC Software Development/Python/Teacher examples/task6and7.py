"""
functions
=========

readFiles()
- Read in the three files and combined into list
- Return combinedList

calculatePercentage()
- combinedList = readFiles()
- for each student in combinedList
-    percentage = (( coursemark + prelimark) / 100) * 150
-    gradeMark = call grade(percentage)
-    add name, percentage, and gradeMark to newList
- displayResults(newList)

grade(percentage)
- Use if statements to discover grade using percentage
- return grade

displayResults(newList)
- countA = 0
- maxPercentage = newlist[0][1]
- for each item in newList
-    if item[2] == "A" then
-        countA += 1
-    if maxPercentage < item[1] then
-        maxPercentage = item[1]
- print(countA)
- print(maxPercentage)

calculatePercentage()



"""