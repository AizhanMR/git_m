data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

# создание пустых списков
letters = []
numbers = []

# сортировка строк
for i in data_tuple:
    letters.append(i) if type(i) == str else numbers.append(i)

# убираем 6.13
numbers.remove(6.13)

# перемещаем True в список letters
letters.append(True)
numbers.remove(True)

# вставляем 2 между 1 и 3 и сортируем
numbers.insert(1, 2)
numbers.sort()

# реверсируем и изменяем пару букв
letters.reverse()
letters[1] = 'Ю'
letters[5] = 'Я'

# возводим в степень
numbers = [int(i) ** 2 for i in numbers]

# из списка делаем кортежи
numbers = tuple(numbers)
letters = tuple(letters)

print(letters)
print(numbers)