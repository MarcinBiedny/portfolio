import sys, random, string

password = []
password_lenght = 0

def correct_data(number):
    while not number.isdigit():
        number = input("It's not a number. ")
    else:
        return int(number)

def update_characters_left(number_of_characters, characters_left):

    while number_of_characters < 0 or number_of_characters > characters_left:
        print("Number of characters out od range 0 -", characters_left)
        number_of_characters = input("Enter a number from the available range. ")
        number_of_characters = correct_data(number_of_characters)
    else:
        characters_left -= number_of_characters
        print("Characters left: ", characters_left)
    return characters_left

while password_lenght < 5:
    password_lenght = input("A good password has at least 5 characters. How long should the password be? ") 
    password_lenght = correct_data(password_lenght) 
else:
    characters_left = password_lenght

lowercase_letters = input("How many lowercase letters should the password have? ")
lowercase_letters = correct_data(lowercase_letters)
characters_left = update_characters_left(lowercase_letters, characters_left)

uppercase_letters = input("How many uppercase letters should the password have? ")
uppercase_letters = correct_data(uppercase_letters)
characters_left = update_characters_left(uppercase_letters, characters_left)

special_characters = input("How many special characters should the password have? ")
special_characters = correct_data(special_characters)
characters_left = update_characters_left(special_characters, characters_left)

digits = input("How many digits should the password have? ")
digits = correct_data(digits)
characters_left = update_characters_left(digits, characters_left)

if characters_left > 0:
    print("Not all characters have been used. The password will be completed with lowercase letters.")
    lowercase_letters += characters_left

print()
print("Password lenght: ", password_lenght)
print("Lowercase letters: ", lowercase_letters)
print("Uppercase letters: ", uppercase_letters)
print("Special characters: ", special_characters)
print("Digits: ", digits)

for _ in range(password_lenght):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -=1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -=1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -=1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Generated password: ", "".join(password))
