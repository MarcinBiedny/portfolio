import sys
import random
import json


def difficulty_level():
    while True:
        difficulty = input("Choose your difficulty level: easy/normal/hard.\n")
        if difficulty.lower() == "easy":
            no_of_tries = int(15)
            break
        elif difficulty.lower() == "normal":
            no_of_tries = int(10)
            break
        elif difficulty.lower() == "hard":
            no_of_tries = int(5)
            break
        else:
            print("Wrong difficulty level. Choose again.")
    print("Number of tries: "+str(no_of_tries))
    return no_of_tries


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_state_of_game(user_word, no_of_tries, used_letters):
    print()
    print(user_word)
    print("Trials left: ", no_of_tries)
    print("Letters used: ", used_letters)
    print()


def random_word():
    with open('yt/python-5-projektow-w-2h/01-hangman_names.json', 'r') as file:
        words = json.load(file)
        word = random.choice(words["names"])
    return word.lower()


def letter_input(used_letters):
    while True:
        letter = input("Enter a letter: ").lower()

        if len(letter) == 1 and letter.isalpha():
            if letter not in used_letters:
                break
            else:
                print("You have already entered that letter.")
        else:
            print("It's not a letter.")
    return letter


def new_game():

    word = random_word()
    used_letters = []
    user_word = []
    no_of_tries = difficulty_level()
    game_finished = False

    for _ in word:
        user_word.append("_")

    while not game_finished:
        letter = letter_input(used_letters)
        used_letters.append(letter)

        found_indexes = find_indexes(word, letter)

        if len(found_indexes) == 0:
            print("There is no such letter.")
            no_of_tries -= 1

            if no_of_tries == 0:
                print("GAME OVER :(")
                game_finished = True
        else:
            for index in found_indexes:
                user_word[index] = letter

            if "".join(user_word) == word:
                print("Bravo, that's the word!")
                game_finished = True

        show_state_of_game(user_word, no_of_tries, used_letters)


print("Welcome to the Hangman game.\nThe game consists in guessing a random male or female name by giving successive letters. Remember that for each misspelled letter you lose one chance.\nGood luck :)")
while True:
    new_game()
    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() != "yes":
        print("Thank you for the game. Goodbye!")
        sys.exit(0)
