# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
# Ввести список одной строкой
    A = list(map(float, input("Введите список:").split()))
# Определить количество элементов списка меньше С
    i = 0
    C = int(input("Введите С:"))
    for item in A:
        if item < C:
            i += 1
    print(f"Колличество элеменнтов больше вееденного числа = {C}")
# Определить сумму элементов списка после последнего отрицательного
    sum = 0
    for item in A:
        if item > 0:
            round(item)
            sum += item
        else:
            sum = 0
    print(f"Сумма элементов после последнего отрицательного элемента списка = {sum}")
# Преобразовать список таким образом, чтобы сначала располагались все элементы,отличающиеся от максимального не более чем на 20%, а потом - все остальные.
    list_2 = []
    list_3 = []
    q = max(A)
    for item in A:
        if  q + (q * 0.2) >= item >= q - (q * 0.2):
            list_2.append(item)
        else:
            list_3.append(item)
    list_sum = list_2 + list_3
    print(list_sum)



