from art import logo
import random
# Include an ASCII art logo.
print(logo)
print("Guess a number between 1 and 100.")
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def difficulty():
    difficulty = input("'Easy' or 'Hard'? ").title()
    if difficulty == 'Easy':
        lives = 10
    elif difficulty == 'Hard':
        lives = 5
    return lives

lives = difficulty()
number = random.randint(1, 100)

while True:
    # Track the number of turns remaining.
    print(f"You have {lives} lives.")
     
    # If they run out of turns, provide feedback to the player. 
    if lives == 0:
        print("Out of lives. Game Over.")
        break
    # Allow the player to submit a guess for a number between 1 and 100.
    guess = int(input("Guess a number between 1 and 100: "))
    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
    if 1 > guess > 100:
        print("Invalid number, guess again.")
    # If they got the answer correct, show the actual answer to the player.
    elif guess == number:
        print(f"The number was {number}.")
        print("You win!")
        end = True
    elif guess < number:
        print("Too low")
        lives -= 1
    elif guess > number:
        print("Too high")
        lives -= 1