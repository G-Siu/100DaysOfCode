# TV Menu
# Date: 14 Dec 2023
# Name: G Siu
# User TV streaming choices

# Display TV menu
print("1. Now TV\n2. NetFlix\n3. Amazon Fire\n4. TV\n5. Exit")
# Ask for user choice
choice = input("Please select: ")
# Check choice conditional
if choice == "1" or choice == "Now TV":
    print("Enjoy watching Now TV!")
elif choice == "2" or choice == "NetFlix":
    print("Enjoy watching NetFlix!")
elif choice == "3" or choice == "Amazon Fire":
    print("Enjoy watching Amazon Fire!")
elif choice == "4" or choice == "TV":
    print("Enjoy watching TV!")
elif choice == "5" or choice == "Exit":
    print("Goodbye, thanks for watching")
else:
    print("Invalid selection")
