# Task: Inventory management system
# Name: G Siu
# Date: 18th April 2024
# Date modified: 18th April 2024

import json

# Load JSON
with open("inventory.json", "r") as f:
    inventory = json.load(f)

# Run until exit
while True:
    print("1. Add a new product\n"
          "2. Update product quantity\n"
          "3. Display current inventory\n"
          "4. Save inventory to JSON file\n"
          "5. Exit")
    user_input = input("Enter option number (1-5): ")
    match user_input:
        case "1":
            print("Add a new product")
            # Get new product details
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            quantity = int(input("Enter quantity: "))
            # Convert to dictionary form
            product = {"name": name,
                       "category": category,
                       "quantity": quantity}
            # Add to inventory
            inventory.append(product)
        case "2":
            print("Update product quantity")
            product_name_to_change = input("Enter name of product: ")
            count = 0  # For indexing inventory list
            for index in inventory:
                # Check if user input is in inventory
                if product_name_to_change in index["name"]:
                    quantity_to_change = int(input("Enter new quantity: "))
                    # Change quantity
                    index["quantity"] = quantity_to_change
                    # Overwrite into inventory
                    inventory[count] = index
                    print("Quantity changed")
                count += 1
        case "3":
            print("Display current inventory\n")
            # Loop through inventory and display
            for product in inventory:
                print(f"Name: {product["name"]}\n"
                      f"Category: {product["category"]}\n"
                      f"Quantity: {product["quantity"]}\n")
        case "4":
            print("Save inventory to JSON file\n")
            # Overwrite existing JSON file with current inventory
            with open("inventory.json", "w") as f:
                json.dump(inventory, f)
            print("Saved to JSON file")
        case "5":
            print("Exiting inventory management system")
            break
            