# Author: Gary Siu
# Date: 5th Feb 2024
# Description: Calculate student grade from coursework and prelim marks

# Function to return coursework marks
def coursework():
    # Initialise variable
    mark = -1
    # Loop until coursework mark within limits
    while mark < 0 or mark > 60:
        # Catch ValueErrors such as strings
        try:
            # Input student coursework mark
            mark = float(input("Enter coursework mark: "))
        except ValueError:
            print("Please use numbers.")
    return mark


# Function to return prelim marks
def prelim():
    # Initialise variable
    mark = -1
    # Loop until prelim mark within limits
    while mark < 0 or mark > 90:
        # Catch ValueErrors such as strings
        try:
            # Input student prelim mark
            mark = float(input("Enter prelim mark: "))
        except ValueError:
            print("Please use numbers.")
    return mark


# Function to calculate mark percentage
def calculate_percentage(coursework_mark, prelim_mark):
    # Use coursework and prelim marks
    return int(((coursework_mark + prelim_mark) * 100) / 150)


# Function to return student grade
def display_grade(coursework, prelim):
    # Pass in marks to calculate_percentage function
    mark_percentage = calculate_percentage(coursework, prelim)
    # IF conditionals to determine grade achieved
    if mark_percentage >= 70:
        return f"Student achieved grade A with total mark of {mark_percentage}"
    elif mark_percentage >= 60:
        return f"Student achieved grade B with total mark of {mark_percentage}"
    elif mark_percentage >= 50:
        return f"Student achieved grade C with total mark of {mark_percentage}"
    elif mark_percentage >= 45:
        return f"Student achieved grade D with total mark of {mark_percentage}"
    else:
        return (f"Student failed to achieve a grade with total mark of "
                f"{mark_percentage}")


def main():
    # Call functions within main
    coursework_mark = coursework()
    prelim_mark = prelim()
    # Pass values returned from coursework and prelim functions into
    # display_grade() and display the result returned
    print(display_grade(coursework_mark, prelim_mark))


# Call main to start the program
main()
