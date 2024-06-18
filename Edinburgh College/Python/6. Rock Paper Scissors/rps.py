import random

# Options list
options = ["Rock", "Paper", "Scissors"]

# List of rules
rules = ["Rock smashes Scissors!", "Paper covers Rock!", "Scissors cut Paper!"]

# Initialise score counts
user_score = 0
computer_score = 0

# Keep game going until user chooses to quit
while True:
    # Get computer's choice
    computer_choice = options[random.randint(0, 2)]

    # Get user choice
    choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s): ")
    # Check user input
    if choice == "r":
        choice = "Rock"
    elif choice == "p":
        choice = "Paper"
    elif choice == "s":
        choice = "Scissors"
    else:
        print("Choose again")
        continue

    # Display choices
    print(f"You chose {choice}, the computer chose {computer_choice}.")

    # Check conditions
    if choice == computer_choice:
        print(f"Both players selected {choice}. It's a tie!")
    elif choice == "Rock":
        if computer_choice == "Paper":
            print(f"{rules[1]} You lose.")
            computer_score += 1
        elif computer_choice == "Scissors":
            print(f"{rules[0]} You win.")
            user_score += 1
    elif choice == "Paper":
        if computer_choice == "Scissors":
            print(f"{rules[2]} You lose.")
            computer_score += 1
        elif computer_choice == "Rock":
            print(f"{rules[1]} You win.")
            user_score += 1
    elif choice == "Scissors":
        if computer_choice == "Rock":
            print(f"{rules[0]} You lose.")
            computer_score += 1
        elif computer_choice == "Paper":
            print(f"{rules[2]} You win.")
            user_score += 1

    # Ask to play again
    user_input = input("Play again? (y/n): ")

    # Continue unless user quits
    if user_input == "y":
        continue
    elif user_input == "n":
        # Display final score
        print(f"Final Scores:\nComputer: {computer_score}\nPlayer: {user_score}")
        break
