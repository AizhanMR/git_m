# Logical data types, conditional construction and

# time = input('enter time - ').lower()
#
# if time == 'morning' or time == 'utro':
#     print("good morning")
# elif time == 'afternoon' or time == 'den':
#     print("good afternoon")
# elif time == 'evening' or time == 'vecher':
#     print("good evening")
# else:
#     print('Hello, (time is not defined!)')

# svetofor = input('svetofor gorit:').lower()
#
# if svetofor == 'red' or svetofor == 'krasny':
#     print("stop")
# elif svetofor == 'yellow' or svetofor == 'jelty':
#     print("wait")
# elif svetofor == 'green' or svetofor == 'zeleny':
#     print("go")
# else:
#     print("ne nesite chepuhu")

temperature = int(input('enter temperature:'))

if -20 <= temperature <= 0:
    print('cold')
elif temperature >= 1 and temperature <= 15:
    print('cool')
elif temperature >= 16 and temperature <= 25:
    print('warm')
elif temperature >= 26 and temperature <= 45:
    print('hot')
else:
    print('how are you even alive?')