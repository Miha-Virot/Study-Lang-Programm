'''
Срез (slice) — извлечение из данной строки одного символа или некоторого фрагмента подстроки или подпоследовательности.

Есть три формы срезов. Самая простая форма среза: взятие одного символа строки, а именно, S[i] — это срез,
состоящий из одного символа, который имеет номер i. При этом считается, что нумерация начинается с числа 0.
То есть если S = 'Hello', то S[0] == 'H', S[1] == 'e', S[2] == 'l', S[3] == 'l', S[4] == 'o'.

Заметим, что в Питоне нет отдельного типа для символов строки. Каждый объект, который получается в результате среза
S[i] — это тоже строка типа str.
Номера символов в строке (а также в других структурах данных: списках, кортежах) называются индексом.

Если указать отрицательное значение индекса, то номер будет отсчитываться с конца, начиная с номера -1.
То есть S[-1] == 'o', S[-2] == 'l', S[-3] == 'l', S[-4] == 'e', S[-5] == 'H'.

Если же номер символа в срезе строки S больше либо равен len(S), или меньше, чем -len(S),
то при обращении к этому символу строки произойдет ошибка IndexError: string index out of range.

Срез с двумя параметрами: S[a:b] возвращает подстроку из b - a символов, начиная с символа c индексом a,
то есть до символа с индексом b, не включая его. Например, S[1:4] == 'ell', то же самое получится если написать
S[-4:-1]. Можно использовать как положительные, так и отрицательные индексы в одном срезе, например,
S[1:-1] — это строка без первого и последнего символа (срез начинается с символа с индексом 1 и заканчиватеся
индексом -1, не включая его).

При использовании такой формы среза ошибки IndexError никогда не возникает. Например, срез S[1:5] вернет
строку 'ello', таким же будет результат, если сделать второй индекс очень большим, например, S[1:100]
(если в строке не более 100 символов).

Если опустить второй параметр (но поставить двоеточие), то срез берется до конца строки.
Например, чтобы удалить из строки первый символ (его индекс равен 0), можно взять срез S[1:].
Аналогично если опустить первый параметр, то можно взять срез от начала строки.
То есть удалить из строки последний символ можно при помощи среза S[:-1]. Срез S[:] совпадает с самой строкой S.

Если задать срез с тремя параметрами S[a:b:d], то третий параметр задает шаг, как в случае с функцией range,
то есть будут взяты символы с индексами a, a + d, a + 2 * d и т. д. При задании значения третьего параметра,
равному 2, в срез попадет кажый второй символ, а если взять значение среза, равное -1, то символы будут идти
в обратном порядке. Например, можно перевернуть строку срезом S[::-1].
'''

s = 'abcdefg'
print(s[1])  # b
print(s[-1])  # g
print(s[1:3])  # bc
print(s[1:-1])  # bcdef
print(s[:3])  # abc
print(s[2:])  # cdefg
print(s[:-1])  # abcdef
print(s[::2])  # aceg
print(s[1::2])  # bdf
print(s[::-1])  # gfedcba
