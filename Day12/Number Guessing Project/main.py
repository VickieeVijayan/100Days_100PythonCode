import random
from art import logo

def random_num():
    return random.uniform(1, 100)

def compare(g_num):
    if g_num > num:
        return "Too High"
    elif g_num < num:
        return "Too Low"

def game(choice):
    for attempt in range(1, choice):
        guess = int(input("Make a guess:   "))
        if guess == num:
            print(f"You got it!! The answer was {num}")
            exit()
        elif guess != num:
            print(compare(guess))
            print("Guess again.")
            print(f"You have {10 - attempt} attempts remaining to guess the number")


def play():
    print(logo)
    print("Welcome to the Number Guessing Game!!")
    print("Im thinking of a number between 1 and 100.")
    print(num)
    u_choice = input("Choose a difficulty. Type 'easy' or 'hard':   ").lower()
    if u_choice == "easy":
        attempts = 10
        game(attempts)
    elif u_choice == "hard":
        attempts = 5
        game(attempts)

num = int(random_num())
is_game_over = False

while not is_game_over:
    play()
    if input("You want to retry? Type 'Y' or 'N':   ").lower() == "n":
        is_game_over = True