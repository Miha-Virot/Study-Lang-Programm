"""
 Однако, во многих задачах нужно именно сохранять всю последовательность, например, если бы нам требовалось
 вывести все элементы последовательности в возрастающем порядке (“отсортировать последовательность”).

Для хранения таких данных можно использовать структуру данных, называемую в Питоне список
(в большинстве же языков программирования используется другой термин “массив”).
Список представляет собой последовательность элементов, пронумерованных от 0, как символы в строке.
"""

Primes = [2, 3, 5, 7, 11, 13]
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# Длину списка, то есть количество элементов в нем, можно узнать при помощи функции len.

a = []  # заводим пустой список
n = int(input())  # считываем количество элемент в списке
for i in range(n):
    new_element = int(input())  # считываем очередной элемент
    a.append(new_element)  # добавляем его в список
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
print(a)

a = []
for i in range(int(input())):
    a.append(int(input()))
print(a)

'''
Обратите особое внимание на последний пример! Очень важная часть идеологии Питона — это цикл for, который предоставляет 
удобный способ перебрать все элементы некоторой последовательности. В этом отличие Питона от Паскаля, 
где вам обязательно надо перебирать именно индексы элементов, а не сами элементы.
Последовательностями в Питоне являются строки, списки, значения функции range() (это не списки), 
и ещё кое-какие другие объекты.

Приведем пример, демонстрирующий использование цикла for в ситуации, когда из строки надо выбрать все цифры и сложить их в массив как числа.
'''
# дано: s = 'ab12c59p7dq'
# надо: извлечь цифры в список digits,
# чтобы стало так:
# digits == [1, 2, 5, 9, 7]

s = 'ab12c59p7dq'
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)
