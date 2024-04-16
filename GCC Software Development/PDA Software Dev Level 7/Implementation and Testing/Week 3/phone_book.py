# Task: Phone Book
# Name: G Siu
# Date: 16th April 2024

# Initialise empty phone book
phone_book = {}


# Function to display names in contacts
def display_names(phone_book):
    # Display contact names
    for name in phone_book.keys():
        print(name)


# Loop the menu until user chooses to quit
while True:
    # Display options
    print("1. Add a new contact\n"
          "2. Update contact information\n"
          "3. Remove a contact\n"
          "4. Check contact existence\n"
          "5. Display all contacts\n"
          "6. Count contacts\n"
          "Or type 'exit' to quit\n")
    # Get user input
    user_input = (input("Choose option 1-6 or 'exit': "))

    # Check user input and execute choice
    match user_input.lower():
        case "1":
            print("Add a new contact")
            name = input("New contact name: ")  # Get new contact name
            # Check if the key already exists, so as not to overwrite
            if name in phone_book.keys():
                print("That name already exists, please use another\n")
            else:
                number = input("Contact phone number: ")  # Get contact phone number
                phone_book[name] = number  # Add to phone book dictionary
        case "2":
            # Go through if phone book is not empty
            if phone_book:
                print("Update contact information")
                # Call names function
                display_names(phone_book)
                # Get contact to update
                existing_contact = input("Enter contact to update: ")
                # If contact exists, perform update
                if existing_contact in phone_book.keys():
                    # Get new number
                    new_number = input("Enter new number for contact: ")
                    phone_book[existing_contact] = new_number  # Update contact
                else:
                    print("No existing contact\n")
            else:
                print("Phone book is empty\n")
        case "3":
            print("Remove a contact")
            # Go through if phone book is not empty
            if phone_book:
                # Call names function
                display_names(phone_book)
                # Get contact to remove
                remove_contact = input("Enter contact to remove: ")
                # Remove contact if it exists
                if remove_contact in phone_book.keys():
                    phone_book.pop(remove_contact)
                    print("Contact removed\n")
                else:
                    print("No existing contact\n")
            else:
                print("Phone book is empty\n")
        case "4":
            print("Check contact existence")
            # Get name from user
            check_contact = input("Contact name: ")
            # Check if contact exists
            if check_contact in phone_book.keys():
                print(f"{check_contact} exists in phone book")
            else:
                print(f"{check_contact} is not in phone book")
        case "5":
            print("Display all contacts")
            # Print all contacts
            for key, value in phone_book.items():
                print(f"{key} - {value}")
            print("")  # Add new line to separate next iteration
        case "6":
            print("Number of contacts")
            print(f"There are {len(phone_book)} contacts in your phone book\n")
        case "exit":
            print("Exiting phone book")
            break
        case _:
            print("Please select one of the options\n")
