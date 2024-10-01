# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
from os import system

print(logo)

dic = {}


def find_highest_bid(data):
    high_bid = 0
    winner = ""
    for name in data:
        if dic[name] > high_bid:
            high_bid = dic[name]
            winner = name

    print(f"The winner is {winner} with a bid of ${high_bid}")

Bids = True
while Bids:
    Name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    dic[Name] = price

    user_input = input("Are there any other bidders? Type 'yes' or 'no'. \n  ").lower()
    if user_input == "no":
        Bids = False
        find_highest_bid(data=dic)
    elif user_input == "yes":
        print("\n" *20)




