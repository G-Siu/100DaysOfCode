from art import logo, vs
from replit import clear
from game_data import data
import random

def game():
    score = 0
    list_a = items()
    list_b = items()
    while list_a == list_b:
        list_b = items()
    while True:
        guess = format(list_a, list_b, vs)
        if guess == 'A' and list_a['follower_count'] > list_b['follower_count']:
            score += 1
            clear()
            print(f"You're right! Current score: {score}")
            list_a, list_b = game_on(list_a, list_b)
        elif guess == 'B' and list_b['follower_count'] > list_a['follower_count']:
            score += 1
            clear()            
            print(f"You're right! Current score: {score}")
            list_a, list_b = game_on(list_a, list_b)
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {score}")
            break
                        
def items():
    return random.choice(data)
    
def format(list_a, list_b, vs):
     print(f"Compare A: {list_a['name']}, {list_a['description']}, from {list_a['country']}.")
     print(vs)
     print(f"Compare B: {list_b['name']}, {list_b['description']}, from {list_b['country']}.")
     return input("Who has more followers? Type 'A' or 'B': ").title()

def game_on(list_a, list_b):
    list_a = list_b
    while list_a == list_b:
        list_b = items()
    return list_a, list_b

def main():
    print(logo)
    game()
    

main()