# daylist = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
#
# # data = {i: int(input(f'enter exp {i.upper()}:')) for i daylist}
# # print(
# #     sum(data.values())
#
# # numbers = [2, 6, 7, 8]
# # numbers = {2, 2, 5, 7, 1}

menu = {
  'lagman': {'noodles', 'meat', 'pepper'},
  'manty': {'meat', 'dough', 'onion'},
  'okroshka': {'kefir', 'kolbasa', 'kartoshka'},
  'greek salad': {'tomato', 'olives', 'onion'}

}
print(input('enter ing'))

# ask = print(input('enter an ingredient'))
# for key in menu:
#     if ask == menu.values():
#         print(menu.keys())
#     else:
#         print('enter ingredients that exist in our database')


# while True:
#     name = input('enter dish name:')
#     if name in menu:
#         print(menu[name])
#     else:
#         print(f' there are no such dishes, but maybe we can interest you with: {tuple(menu.keys())}')
#
# print(lagman - manty)
# print(lagman.difference(manty))
# print(lagman.intersection(manty))
# print(lagman.union(manty))
# print(lagman.symmetric_difference(manty))


# print(sum([5, 6, 90, 54]))
# print(min([5, 6, 8, 9]))

# print(type(student))
#
# print(dict(enumerate('python')))

# student = {
#     (0, 3, 5): 5,
#     23: 5,
#     5.6: 67,
#     True: 45,
#     'string': 5
# }
# new = dict(name='Azula', surname= 'Nol', age=29, country='China')
#
# student = {
#     'name': 'Aizhan',
#     'height': 1.80,
#     'age': 19,
#     'haveacar': False,
#     'hobby': ['chess', 'english', 'math', 'books'],
#     'education': ('school', 'university')

# print(student['education'])
# print(student.get('educ'))
# print(student.keys())
# print(student.values())
# print(student.items())
# # for i in student:
#     print(i, '==>', student[i])

# for key, value in student.items():
#     print(f'{key}: {value})
# '''add'''
# student['surname'] = 'Li'
# student.update(new)
#
# '''edit'''
# student['age'] += 1
# student['haveacar'] = True
# student['hobby'][-2] = 'football'
#
# '''delete'''
# del student['hobby'][2]
# student.pop('haveacar')
#
#
# print(student)

