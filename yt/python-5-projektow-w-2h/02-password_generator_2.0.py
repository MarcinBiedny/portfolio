import sys, random, string

password = []
password_lenght = 0

def get_new_number_from_user():
    while True:
        number = input("It's not a number. ")
        if number.isdigit():
            break

    return int(number)

def update_characters_left(number_of_characters, characters_left):

    while number_of_characters < 0 or number_of_characters > characters_left:
        print("Number of characters out od range 0 -", characters_left)
        number_of_characters = input("Enter a number from the available range. ")
        number_of_characters = get_new_number_from_user() if not number_of_characters.isdigit() else int(number_of_characters)
    else:
        characters_left -= number_of_characters
        print("Characters left: ", characters_left)
        
    return int(characters_left)

while int(password_lenght) < 5:
    password_lenght = input("A good password has at least 5 characters. How long should the password be? ")
    password_lenght = get_new_number_from_user() if not password_lenght.isdigit() else int(password_lenght)
else:
    characters_left = password_lenght

count_of_lower_case_letters_in_password = input("How many lowercase letters should the password have? ")
count_of_lower_case_letters_in_password = get_new_number_from_user() if not count_of_lower_case_letters_in_password.isdigit() else int(count_of_lower_case_letters_in_password)
characters_left = update_characters_left(count_of_lower_case_letters_in_password, characters_left)

count_of_upper_case_letters_in_password = input("How many uppercase letters should the password have? ")
count_of_upper_case_letters_in_password = get_new_number_from_user() if not count_of_upper_case_letters_in_password.isdigit() else int(count_of_upper_case_letters_in_password)
characters_left = update_characters_left(count_of_upper_case_letters_in_password, characters_left)

count_of_special_characters_in_password = input("How many special characters should the password have? ")
count_of_special_characters_in_password = get_new_number_from_user() if not count_of_special_characters_in_password.isdigit() else int(count_of_special_characters_in_password)
characters_left = update_characters_left(count_of_special_characters_in_password, characters_left)

count_of_digist_in_password = input("How many digits should the password have? ")
count_of_digist_in_password = get_new_number_from_user() if not count_of_digist_in_password.isdigit() else int(count_of_digist_in_password)
characters_left = update_characters_left(count_of_digist_in_password, characters_left)

if characters_left > 0:
    print("Not all characters have been used. The password will be completed with lowercase letters.")
    count_of_lower_case_letters_in_password += characters_left

print()
print("Password lenght: ", password_lenght)
print("Lowercase letters: ", count_of_lower_case_letters_in_password)
print("Uppercase letters: ", count_of_upper_case_letters_in_password)
print("Special characters: ", count_of_special_characters_in_password)
print("Digits: ", count_of_digist_in_password)

for _ in range(password_lenght):
    if count_of_lower_case_letters_in_password > 0:
        password.append(random.choice(string.ascii_lowercase))
        count_of_lower_case_letters_in_password -=1
    if count_of_upper_case_letters_in_password > 0:
        password.append(random.choice(string.ascii_uppercase))
        count_of_upper_case_letters_in_password -=1
    if count_of_special_characters_in_password > 0:
        password.append(random.choice(string.punctuation))
        count_of_special_characters_in_password -=1
    if count_of_digist_in_password > 0:
        password.append(random.choice(string.digits))
        count_of_digist_in_password -= 1

random.shuffle(password)
print("Generated password: ", "".join(password))
