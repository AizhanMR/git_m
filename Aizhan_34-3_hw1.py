# ввод расходов пользователем
Mon = int(input('Введите ваши расходы за понедельник'))
Tue = int(input('Введите ваши расходы за вторник'))
Wed = int(input('Введите ваши расходы за среду'))
Thu = int(input('Введите ваши расходы за четверг'))
Fri = int(input('Введите ваши расходы за пятницу'))
Sat = int(input('Введите ваши расходы за субботу'))
Sun = int(input('Введите ваши расходы за воскресенье'))

# калькуляция итога за неделю
total = Mon + Tue + Wed + Thu + Fri + Sat + Sun
print('Ваши общие расходы за неделю:', total)

# калькуляция среднего расхода в день
average = round(total/7, 1)
print('Ваш средний расход в день:', average)

print('Не траньжирте деньги :)')