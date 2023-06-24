"""
- translate the game into English - check
- validation (letters only)
- do not allow repeated letters
- word list to guess
- drawing a word from the list (no repetitions in subsequent games)
- select restart/quit game
- selection of the number of chances / game difficulty level - check
"""

import sys

#global no_of_tries
#no_of_tries = 5
word = "marcin"
used_letters = []

user_word =[]

def difficulty_level():
    global no_of_tries
    while True:
        difficulty = input("Choose your difficulty level: easy/normal/hard.\n")
        if difficulty.lower() == "easy":
            no_of_tries = int(7)
            break
        elif difficulty.lower() == "normal":
            no_of_tries = int(5)
            break
        elif difficulty.lower() == "hard":
            no_of_tries = int(3)
            break
        else:
            print("Wrong difficulty level. Choose again")
    print("Number of tries: "+str(no_of_tries))
    return no_of_tries

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Trials left: ", no_of_tries)
    print("Letters used: ", used_letters)
    print()

def new_game():
    difficulty_level()
    global no_of_tries
    for _ in word:
        user_word.append("_")

    while True:
        letter = input("Enter a letter: ")
        used_letters.append(letter)

        found_indexes = find_indexes(word, letter)

        if len(found_indexes) == 0:
            print("There is no such letter.")
            no_of_tries -=1

            if no_of_tries == 0:
                print("GAME OVER :(")
                sys.exit(0)
        else:
            for index in found_indexes:
                user_word[index] = letter
        
            if "".join(user_word) == word:
                print("Bravo, that's the word!")
                sys.exit(0)

        show_state_of_game()

new_game()