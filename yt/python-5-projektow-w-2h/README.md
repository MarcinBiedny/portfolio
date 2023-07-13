# "Python - 5 projektów w 2h"
My progress on ["Python - 5 projektów w 2h"](https://www.youtube.com/watch?v=EFaPsPwPJAY) youtube course in Polish.

Progress branch: **python/yt/python-5-projektow-w-2h**

## Hangman
A game of guessing Polish names by entering consecutive letters that should be in the searched password.

### 01-hangman_1.0.py
The basic version of the game with a predetermined password to guess and a defined number of try.

### 01-hangman_2.0.py
An extended version of the game with additional options such as choosing the difficulty level and a random password to guess.

Main goals:
- game is fully in English language
- validation for only letters input is in place
- validation for input repetition is in place (same letters are not allowed to be input twice)
- configurable words list in the form of json file
- drawing a word from the list
- ability to restart/quit game
- selection of the number of chances / game difficulty level

## Password generator
A program for generating random passwords based on the number of characters declared by the user and the number of lowercase letters, uppercase letters, special characters and numbers.

### 02-password_generator_1.0.py
The basic version of the program.

### 02-password_generator_2.0.py
Extended version of the program.

Main goals:
- program is fully in English language
- removing global variables
- validation for only digits input
- validation for entering digits from the available range
- validation for minimum password length
