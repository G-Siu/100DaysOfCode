"""
1.1 PRINT enter students coursework mark
1.2 DO
1.3    GET courseWorkMark
1.4 WHILE < 0 OR > 60

2.1 PRINT enter students prelim mark
2.2 DO
2.3    GET prelimMark
2.4 WHILE < 0 OR > 90
"""
# Author: Gary Siu
# Date: 5th Feb 2024
# Description:

# Initialise coursework mark variable
coursework_mark = -1
# Loop until coursework mark within limits
while coursework_mark < 0 or coursework_mark > 60:
    # Input student coursework mark
    coursework_mark = float(input("Enter coursework mark: "))

# Initialise prelim mark variable
prelim_mark = -1
# Loop until prelim mark within limits
while prelim_mark < 0 or prelim_mark > 90:
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
elif mark_percentage >= 45:
    print("Student achieved grade D with total of", mark_percentage)
else:
    print("Student failed to achieve a grade with total of", mark_percentage)
