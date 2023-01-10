import csv

with open("dictionary.csv", "r") as file:
    reader = csv.reader(file)
    dictionary = {
        row[0]: row[1]
        for row in reader
    }


def eng_to_rus(word):
    return dictionary.get(word, "ERROR")


def rus_to_eng(asd):
    return {
        value: key
        for key, value in dictionary.items()
    }.get(asd, "ERROR")


def rus_to_eng_2(word):
    for eng, rus in dictionary.items():
        if rus == word:
            return eng


print(eng_to_rus("apple"))
print(rus_to_eng("зеленый"))