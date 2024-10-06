import random
from game_data import data
from art import logo, vs

def pick():
    r_pick = random.choice(data)
    return r_pick

# TODO: Compare those 2 and provide the result
def compare(option):
    if option == "a" and compare_a["follower_count"] > against_b["follower_count"]:
        return 1
    elif option == "b" and compare_a["follower_count"] < against_b["follower_count"]:
        return 1
    elif compare_a["follower_count"] == against_b["follower_count"]:
        return 1
    else:
        return 0

# TODO: TO pick 2 random list from the dictionary
print(logo)
score = 0
compare_a = pick()
game_over = False
while not game_over:
    print(f"Compare A: {compare_a["name"]}, {compare_a["description"]}, {compare_a["country"]}")
    print(vs)
    against_b = pick()
    print(f"Against B: {against_b["name"]}, {against_b["description"]}, {against_b["country"]}")
    choice = input("Who has more followers? Type 'A' or 'B':     ").lower()
    print(logo)
    turn = compare(choice)
    if turn == 0:
        print(f"Sorry, that's wrong. Final Score: {score}.")
        game_over = True

    # TODO: Keep adding the score and 1 random until user choose wrong option
    else:
        compare_a = against_b
        score += 1
        print(f"You're right! Current Score: {score}.")
