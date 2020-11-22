# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
# Ввести список одной строкой
    A = list(map(int, input("Введите список из 10 элементов(через пробел):").split()))
# Проверить количество элементов списка
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
# Найти искомое произведение
    r = 1
    for item in A:
            if item >= 0:
                r *= item
    print(r)
