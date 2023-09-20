import json, random
        
def show_question(question, points):
    print()
    print(question["question"])
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

    if answer == question["correct_answer"]:
        points += 1
        print()
        print("Brawo! This is the correct answer. You already have" , points, "points.")
    else:
        print()
        print("Unfortunately this is the wrong answer, the correct answer is " + question["correct_answer"].upper() + ".")

    return points

def game():

    print()
    print("Welcome to the Quiz.")
    print("The game involves answering questions by selecting the correct answer from among the four available.")
    print("Good luck :)")
    print()

    points = 0

    with open("yt/python-5-projektow-w-2h/03-quiz_2.0.json") as json_file:
        questions = json.load(json_file)

    while True:
        available_category = questions.keys()
        category = input("What category would you like to receive questions from: " + ", ".join(available_category) + "?\n").lower()
        if category in (available_category):
            break
        else:
            print("There is no such category.")

    questions = questions[str(category)]

    random.shuffle(questions)
    for i in range(0, len(questions)):
        points = show_question(questions[i], points)

    print()
    print("It's game over. Number of points scored - " + str(points) + ".")

game()
