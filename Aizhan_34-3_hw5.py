Geeks = {

    'address': 'Toktogula 175',

    'courses': ['Android', 'Backend', 'Frontend'],

    'bag': {'fails', 'errors', 'stack'}

}

# удалить bag
del Geeks['bag']

# добавить адрес и контактные данные
Geeks['address'] = 'Ibraimova 103'
Geeks['contacts'] = 'instagram: @geeks_edu / phone number: +996507052018'

# добавляем курсы и изменяем на сет
Geeks['courses'].append('UX/UI')
Geeks['courses'].append('IOS')
Geeks['courses'] = set(Geeks['courses'])

# дата основания
Geeks['foundation date'] = '05.05.2018'

# выводим на экран в формате ключ:значение
for key, value in Geeks.items():
    print(f'{key}: {value}')

# количество курсов
print('number of available courses:', len(Geeks[('courses')]))
