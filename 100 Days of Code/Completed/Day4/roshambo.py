# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: ")
if choice == '0':
  print(rock)
elif choice == '1':
  print(paper)
elif choice == '2':
  print(scissors)

computer = random.randint(0, 2)
computer = str(computer)
if computer == '0':
  print("Computer chose:\n" + rock)
elif computer == '1':
  print("Computer chose:\n" + paper)
elif computer == '2':
  print("Computer chose:\n" + scissors)

if choice == '0' and computer == '2':
  print("You win")
elif choice == '1' and computer == '0':
  print("You win")
elif choice == '2' and computer == '1':
  print("You win")
elif choice == computer:
  print("Draw")
else:
  print("You lose")