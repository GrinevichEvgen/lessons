import random

original_n = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
original_m = ["H", "D", "C", "S"]


def get_random_card():
    random_n = random.choice(original_n)
    random_m = random.choice(original_m)
    return random_n, random_m


my_dict = {
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 2, "D": 3, "K": 4, "A": 1
}


def nominal_to_value(nominal):
    return my_dict[nominal]


used_cards = []
current_sum = 0
while True:
    choice = input("Достать следующую карту [Y/n]: ")
    if choice == "n":
        break

    current_card = None
    while True:
        n, m = get_random_card()
        current_card = f"{n}-{m}"
        if current_card not in used_cards:
            used_cards.append(f"{n}-{m}")
            break

    print("Текущая карта: ", current_card)
    current_sum += nominal_to_value(n)
    if current_sum > 21:
        print("Game over, ты проиграл, твоя текущая сумма: ", current_sum)
        break

    if current_sum == 21:
        print("Ты выйграл")
        break

    if current_sum < 21:
        print("Твоя текущая сумма: ", current_sum)
