"""
- przetłumaczenie gry na język angielski
- usunięcie zmiennej globalnej
- walidacja (wybór tylko a,b,c,d) - możliwość poprawy
- losowość pytań
- możliwość wybory kategorii/poziomu trudności pytania

"""

import json

points = 0

def show_question(question):
    global points
    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer = input("Którą odpowiedź wybierasz? ")

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print("To prawidłowa odpowiedz, brawo! Masz już" , points, "punktów.")
    else:
        print("Niestety to zła odpowiedź, prawidłowa odpowiedź to " + question["prawidlowa_odpowiedz"] + ".")


with open("yt/python-5-projektow-w-2h/03-quiz.json") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        show_question(questions[i])

print()
print("To koniec gry, zdobyta liczba punktów to " + str(points) + ".")