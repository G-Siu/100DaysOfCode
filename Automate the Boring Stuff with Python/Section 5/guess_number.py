# Guess a number game
import random

name = input("Hello. What is your name?\n")
print("Well, " + name + ", I am thinking of a number between 1 and 20.")
secret_num = random.randint(1, 20)

for guesses in range(1, 7):
    guess = int(input("Take a guess.\n"))
    if guess < secret_num:
        print("Your guess is too low.")
    elif guess > secret_num:
        print("Your guess is too high.")
    else:
        break

if guess == secret_num:
    print("Good job, " + name + "! You guessed my number in " + str(guesses) + " guesses.")
else:
    print("Nope. The number I was thinking of was " + str(secret_num) + ".")
