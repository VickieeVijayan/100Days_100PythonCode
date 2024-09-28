import random
from D7hangman_words import word_list
from D7hangman_art import logo, stages

lives = 6

# Print the logo
print(logo)

# Choosing random word from hangman_words.py program
chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO: - Prints how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"letter {guess} is already guessed")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not in the word. You lose a life")

        if lives == 0:
            game_over = True

            # TODO: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************It was a {chosen_word}!! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
