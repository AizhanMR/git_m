# grade = int(input('Enter your grade '))
# attendance = int(input('enter percentage of your attendance '))
#
# if grade >= 90 and attendance >= 80:
#     print('A')
# elif grade >= 75 and attendance >= 70 or grade >= 70 and attendance >= 80:
#     print('B')
# elif grade >= 65 and attendance >= 60 or grade >= 60 and attendance >= 70:
#     print('C')
# elif grade < 65 and attendance < 60 or grade attendance < 60:
#     print('D')
# elif grade < 50 and attendance < 40:
#     print('no passing grade')

p = 0
while True:
    p += 1
    per = int(input('enter a number'))

    if per > 10:
        print('>10')
    elif per == 10:
        print('=10')
    elif per < 10:
        print('<10')
    else:
        print('none')