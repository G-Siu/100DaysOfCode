from replit import clear
from art import logo

print(logo)
bid_list = {}
while True:    
    name = input("Your name: ")
    bid = int(input("Your bid: $"))
    bid_list[name] = bid
    loop = input("More bidders? Type 'yes'. Otherwise 'no'. ")
    if loop == 'no':
        high_bid = 0
        for key in bid_list:
            current_bid = bid_list[key]
            if current_bid > high_bid:
                high_bid = current_bid
                winner = key
        print(f"The winner is {winner} with a bid of ${high_bid}")
        break
    elif loop == 'yes':
        clear()