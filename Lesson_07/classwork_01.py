'''Известно, что на шахматной доске 8×8 можно расставить ферзей так, чтобы они не били друг друга
(ферзь может ходить по горизонтали, вертикали и диагонали). Вам дана расстановка двух ферзей на доске,
 определите могут ли ферзи бить друг друга. Программа получает на вход две пары чисел,
 первое число в паре - координата по горизонтали, второе - координата по вертикали.
 Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.'''

first = [3,7]
last = [4,6]

if __name__ =="__main__":
    if first[0]==last[0] or first[1]==last[1]:
        print("YES")
    if abs(first[0] - last[0]) == abs(first[1] - last[1]):
        print("NO")