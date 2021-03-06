'''
Метод — это функция, применяемая к объекту, в данном случае — к строке.
Метод вызывается в виде Имя_объекта.Имя_метода(параметры).
Например, S.find("e") — это применение к строке S метода find с одним параметром "e".

Метод find находит в строке (к которой применяется метод) подстроку (которая передается в качестве параметра).
Функция возвращает индекс первого вхождения искомой подстроки.
Если же подстрока не найдена, то метод возвращает значение -1.
'''
S = 'Hello'
print(S.find('e'))
# вернёт 1
print(S.find('ll'))
# вернёт 2
print(S.find('L'))
# вернёт -1

#Аналогично, метод rfind возвращает индекс последнего вхождения данной строки (“поиск справа”).
S = 'Hello'
print(S.find('l'))
# вернёт 2
print(S.rfind('l'))
# вернёт 3

'''
Если вызвать метод find с тремя параметрами S.find(T, a, b),
то поиск будет осуществляться в срезе S[a:b].
Если указать только два параметра S.find(T, a),
то поиск будет осуществляться в срезе S[a:],
то есть начиная с символа с индексом a и до конца строки.
Метод S.find(T, a, b) возращает индекс в строке S, а не индекс относительно среза.
'''





#Метод replace заменяет все вхождения одной строки на другую.
# Формат: S.replace(old, new) — заменить в строке S все вхождения подстроки old на подстроку new.
print('Hello'.replace('l', 'L'))
# вернёт 'HeLLo'

#Если методу replace задать еще один параметр: S.replace(old, new, count),
# то заменены будут не все вхождения, а только не больше, чем первые count из них.
print('Abrakadabra'.replace('a', 'A', 2))
# вернёт 'AbrAkAdabra'





#Подсчитывает количество вхождений одной строки в другую строку.
# Простейшая форма вызова S.count(T)  возвращает число вхождений строки T внутри строки S.
# При этом подсчитываются только непересекающиеся вхождения/
print('Abracadabra'.count('a'))
# вернёт 4
print(('a' * 10).count('aa'))
# вернёт 5
# При указании трех параметров S.count(T, a, b), будет выполнен подсчет числа вхождений строки T в срезе S[a:b].





#Элементы списка могут вводиться по одному в строке, в этом случае строку целиком
# можно считать функцией input(). После этого можно использовать метод строки split(),
# возвращающий список строк, которые получатся, если исходную строку разрезать на части по пробелам.

# на вход подаётся строка
# 1 2 3
s = input()  # s == '1 2 3'
a = s.split()  # a == ['1', '2', '3']

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

a = [int(s) for s in input().split()]

#У метода split() есть необязательный параметр, который определяет,
# какая строка будет использоваться в качестве разделителя между элементами списка.
a = '192.168.0.1'.split('.')





# В Питоне можно вывести список строк при помощи однострочной команды.
# Для этого используется метод строки join. У этого метода один параметр: список строк.
# В результате возвращается строка, полученная соединением элементов переданного списка
# в одну строку, при этом между элементами списка вставляется разделитель, равный той строке,
# к которой применяется метод.

a = ['red', 'green', 'blue']
print(' '.join(a))
# вернёт red green blue
print(''.join(a))
# вернёт redgreenblue
print('***'.join(a))
# вернёт red***green***blue

a = [1, 2, 3]
print(' '.join([str(i) for i in a]))
# следующая строка, к сожалению, вызывает ошибку:
# print(' '.join(a))
