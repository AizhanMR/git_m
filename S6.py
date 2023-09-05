# functions arguments: *args, **kwargs

# oпределение наименование(параметры)
#      тело функции
#      возвращение результата
#
# наименование(аргументы)
# students = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
numbers = [2, 3, 1]
def suma(numbers):
    amount = 0
    for i in numbers:
        amount += i
    return amount

print(suma(numbers))

def maximum(numbers):
    v = 0
    for i in numbers:
        v += 1
        if numbers > v:
            v = numbers

print(maximum(numbers))




# def amount(items):
#     counter = 0
#     for i in items:
#         counter += 1
#     return counter
#
# print(amount(students))
# width = 5
# length = 8
#
# square_2 = width * length
#
# width = 12
# length = 18
#
# square_hall = width * length
# print(square_2)
# print(square_hall)
