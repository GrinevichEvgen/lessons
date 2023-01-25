'''Головоломка “Ханойские башни” состоит из трех стержней,пронумерованных числами 1, 2, 3.
На стержень 1 надета пирамидка из n дисков различного диаметра в порядке возрастания диаметра.
Диски можно перекладывать с одного стержня на другой строго по одному,
при этом диск нельзя класть на диск меньшего диаметра.
Необходимо переложить всю пирамидку со стержня 1 на стержень 3 за минимальное число перекладываний.
Необходимо написать программу, которая для данного числа дисков n печатает последовательность перекладываний,
необходимую для решения головоломки.'''

def hanoi(n, a, b): # a-старт,b- финиш
    if n == 1:
        print("Перенести диск 1 со стержня", a, "на стержень", b)
    else:
        temp = (6 - a) - b   #промежуточный стержень
        hanoi(n - 1, a, temp)
        print("Перенести диск", n, "со стержня", a, "на стержень", b)
        res = (n - 1, temp, b)
        print(res)

        return res

if __name__ == '__main__':
    assert hanoi(3, 1, 3)# (кол-во дисков, a , b )