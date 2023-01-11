'''Написать программу, которая выведет на экран все числа от 1 до 100 которые кратные n
(n вводится с клавиатуры).'''




my_dict = {0:[],1:[],2:[]}



for index, lst in dict.items():
    while True:
        current_simbol = input()
        if current_simbol.isnumeric():
            lst.append(current_simbol)

        else:
            break
            print(my_dict)

            all_element = set(my_dict[0]+my_dict[1]+my_dict[2])
            new_list = []
            if element in all_element:
                if element in mi_dict[0] and element in mi_dict[1] and element not in my_dict[2]:
                    new_list.append(element)
                    print(new_list)

