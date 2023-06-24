"""
- translate the game into English - check
- validation (letters only)
- do not allow repeated letters
- word list to guess
- drawing a word from the list (no repetitions in subsequent games)
- select restart/quit game - check
- selection of the number of chances / game difficulty level - check
"""

import sys

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
                game_restart()
        else:
            for index in found_indexes:
                user_word[index] = letter
        
            if "".join(user_word) == word:
                print("Bravo, that's the word!")
                game_restart()
            
        show_state_of_game()

def game_restart():
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == "no":
            print("Thank you for the game. Goodbye!")
            sys.exit(0)
        elif choice.lower() == "yes":
            global used_letters
            global user_word
            used_letters = []
            user_word = []
            new_game()

new_game()