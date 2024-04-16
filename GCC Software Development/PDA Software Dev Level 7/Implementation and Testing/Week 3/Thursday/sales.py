# coding=utf-8
# Task: Load CSV and calculate total sales per category
# Name: G Siu
# Date: 16th April 2024

import csv

# Initialise empty dictionary
products = {}

# Open CSV file
with open("sales.csv", "r") as f:
    content = csv.reader(f)  # Load CSV file to variable
    # Loop through list
    for row in content:
        # Disregard header line
        if row[1] != "Category":
            # Check if category already exists
            if row[1] not in products:
                # Create new key with respective value
                products[row[1]] = int(row[2])
            else:
                # Add to existing key, value
                products[row[1]] += int(row[2])

for category, sales in products.items():
    print(f"Total sales in {category} is £{sales}.")
    