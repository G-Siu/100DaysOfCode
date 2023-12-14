# Task - ELIF - Multiple IF
# Date: 13 Dec 2023
# Name: G Siu

"""Algorithm - Determine exam grade
1. Input name
2. Input exam mark
3. If exam mark is greater than or equal to 70, say achieved grade A
4. If exam mark is greater than or equal to 60, say achieved grade B
5. If exam mark is greater than or equal to 50, say achieved grade C
6. Else say has failed
"""

# Ask for name and exam mark
name = input("Name: ").title()
exam_mark = int(input("Exam mark: "))

# Conditions dependent on exam mark
if exam_mark >= 70:
    print(name, "achieved grade A")
elif exam_mark >= 60:
    print(name, "achieved grade B")
elif exam_mark >= 50:
    print(name, "achieved grade C")
else:
    print(name, "has failed")
