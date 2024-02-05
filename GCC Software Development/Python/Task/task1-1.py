"""
1. input one student’s coursework mark
2. input one student's prelim mark
3. calculate percentage = ((coursework mark + prelim mark) *100) / 150
4. display grade using a series of IF statements
"""
# Author: Gary Siu
# Date: 5th Feb 2024
# Description: Calculate Student Marks

# Input student coursework mark
coursework_mark = float(input("Enter coursework mark: "))
# Input student prelim mark
prelim_mark = float(input("Enter prelim mark: "))
# Calculate percentage
mark_percentage = int(((coursework_mark + prelim_mark) * 100) / 150)

# Display grade with IF conditionals
if 100 >= mark_percentage >= 70:
    print("Student achieved grade A with total of", mark_percentage)
elif mark_percentage >= 60:
    print("Student achieved grade B with total of", mark_percentage)
elif mark_percentage >= 50:
    print("Student achieved grade C with total of", mark_percentage)
elif mark_percentage >= 40:
    print("Student achieved grade D with total of", mark_percentage)
else:
    print("Student failed to achieve a grade with total of", mark_percentage)

