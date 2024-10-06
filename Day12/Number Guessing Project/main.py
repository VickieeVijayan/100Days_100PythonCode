import random
from art import logo

def random_num():
    return random.randint(1, 100)

def compare(g_num, a_num, left):
    if g_num > a_num:
        print("Too High.")
        return left - 1
    elif g_num < a_num:
        print("Too Low.")
        return left - 1
    elif g_num == a_num:
        print(f"You got it!! The answer was {g_num}")
        return 0

def game(level):
    while level != 0:
            print(f"You have {level} attempts remaining to guess the number ")
            guess = int(input("      Make a guess:   "))
            level = compare(guess, num, level)
            if level == 0 and guess != num:
                print(f"It was {num} ^x^ ")
            elif level > 0:
                print("Try again.")



def play():
    print(logo)
    print("Welcome to the Number Guessing Game!!")
    print("Im thinking of a number between 1 and 100.")
    #print(num)
    u_choice = input("Choose a difficulty. Type 'easy' or 'hard':   ").lower()
    if u_choice == "easy":
        game(EASY_LEVEL)
    elif u_choice == "hard":
        game(HARD_LEVEL)

HARD_LEVEL = 5
EASY_LEVEL = 10
is_game_over = False

while not is_game_over:
    num = random_num()
    play()
    if input("You restart a new game? Type 'Y' or 'N':   ").lower() == "n":
        is_game_over = True