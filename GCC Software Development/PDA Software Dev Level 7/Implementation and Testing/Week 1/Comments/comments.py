# Task: Practice commenting
# Name: G Siu
# Date: 18th March 2024

# Import modules
import os
import random


# Function to get full name
def enter_name():
    full_name = input("Please enter your full name: ")
    return full_name


# Function that takes the full name parameter and splits them
def split_name(full_name):
    # Split the full name
    names = full_name.split()
    # Get first name
    first_name = names[0]
    # Get last name
    last_name = names[-1]
    return first_name, last_name


# Function that returns the first character in the first name
def first_char(first_name):
    # Get first character in first name
    f_char = first_name[0]
    return f_char


# Function that returns a random number between 100 and 999
def random_number():
    # Get a random number between 100 and 999
    number = random.randrange(100, 999)
    return number


# Call enter_name function and store in full_name
full_name = enter_name()
# Store first and last name from split_name function
first_name, last_name = split_name(full_name)
# Create a username
user_name = first_char(first_name).lower() + last_name + str(random_number())
print(f"The username for {full_name} is {user_name}")
