# Task - IF using boolean
# Date: 13 Dec 2023
# Name: G Siu

""" Algorithm - Determine pet insurance
1. Input type of insurance
2. If either cat or dog, say "Quote is £10pcm"
3. Else say "Quote is £25pcm"
"""

user_input = input("Type of pet insurance? ").lower()
if user_input == "cat" or user_input == "dog":
    print("Quote is £10pcm")
else:
    print("Quote is £25pcm")
