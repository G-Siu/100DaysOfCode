# Conversions Revision Exercise
# Date: 07 Dec 2023
# Name: G Siu
# Convert cm to inches

# Ask for cm
cm = float(input("Enter measurement in cm to be converted to inches: "))
# Calculate inches
inches = cm / 2.54
# Display converted measurement
print(f"Converted {cm} to {"{0:.2f}".format(inches)}")
