import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculation(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Opponent has a blackjack, You loss"
    elif u_score == 0:
        return "It's blackjack, you win"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You loss"

def play_game():
    print(logo)
    user_card = []
    comp_card = []
    user_score = -1
    comp_score = -1
    for _ in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card())

    is_game_over = False
    while not is_game_over:
        user_score = calculation(user_card)
        comp_score = calculation(comp_card)

        print(f" Your cards: {user_card} and your score: {user_score}")
        print(f" Computer's first card: {comp_card[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_card.append(deal_card())
        comp_score = calculation(comp_card)

    print(f"Final hand: {user_card} Final score: {user_score}")
    print(f"Final computer hand: {comp_card}, Final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()

# import random
# from art import logo
#
#
# cards = [11,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# def user_cards():
#     user_picked_cards = random.sample(cards, 1)
#     return user_picked_cards
#
# def comp_cards():
#     computer_cards = random.sample(cards, 1)
#     return computer_cards
#
# def score(card):
#     if sum(card) == 21 and len(card) == 2:
#         return 0
#     return sum(card)
#
# def pick_cards():
#     print(logo)
#     user_pick = user_cards()
#     comp_pick = comp_cards()
#     user_choice = True
#     while user_choice:
#         user_pick += user_cards()
#         user_score = score(user_pick)
#         if user_score > 21:
#             print(f"    Your Card: {user_pick} and Current score: {user_score}")
#             print(f"    Computer's first card: {comp_pick}")
#             print(f"    Your Final hand: {user_pick} and final score: {user_score}")
#             print(f"    Computer's final hand: {comp_pick} and final score: {comp_pick}")
#             print("You went over. You Lose😭")
#             user_choice = False
#             return user_choice
#         print(f"    Your Card: {user_pick} and Current score: {user_score}")
#         print(f"    Computer's first card: {comp_pick}")
#         choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#         if choice == "n":
#             user_choice = False
#             comp_pick += comp_cards()
#             comp_score = score(comp_pick)
#             while comp_score < 17:
#                 comp_pick += comp_cards()
#                 comp_score = score(comp_pick)
#                 if comp_score > 21:
#                     comp_pick.pop()
#                     comp_score = score(comp_pick)
#
#             print(f"    Your Final hand: {user_pick} and final score: {user_score}")
#             print(f"    Computer's final hand: {comp_pick} and final score: {comp_score}")
#             if user_score > comp_score:
#                 print("You win!! 😊")
#             elif user_score == comp_score:
#                 print("Draw 😢")
#             else:
#                 print("Computer won!! 😢")
#
# user_choice1 = True
# while user_choice1:
#     choice1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
#     if choice1 == "y":
#         pick_cards()
#     elif choice1 == "n":
#         print("Game Over, Bye!!")
#         user_choice1 = False