"""
- translate into English - check
- remove global variables - check
- validation of entered answers - check
- category selection
- random order of questions - check
"""

import json, random
        
def show_question(question, points):
    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    while True:
        answer = input("Which answer do you choose? ").lower()
        if answer in ["a", "b", "c", "d"]:
            break
        else:
            print("Incorrect selection. Choose the answer: a, b, c or d.")

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print()
        print("Brawo! This is the correct answer. You already have" , points, "points.")
    else:
        print()
        print("Unfortunately this is the wrong answer, the correct answer is " + question["prawidlowa_odpowiedz"] + ".")

    return points

def game():
    points = 0

    with open("yt/python-5-projektow-w-2h/03-quiz_1.0.json") as json_file:
        questions = json.load(json_file)

    random.shuffle(questions)
    for i in range(0, len(questions)):
        points = show_question(questions[i], points)

    print()
    print("It's game over. Number of points scored - " + str(points) + ".")

game()
