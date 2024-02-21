import random

reindeer = ["dasher", "dancer", "prancer",
            "vixen", "comet", "cupid",
            "donner", "blitzen", "rudolph"]

random_reindeer = random.choice(reindeer)

guess = input("Guess the name of Santa's reindeer : ").lower()

if random_reindeer == guess :
    print("You picked a correct amswer")
else :
    print("You are on the naught list")

print(f"The correct answer was {random_reindeer}")