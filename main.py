# brick = [23, 'loophole', 0, 'great', True, 67, False]
#
# brick.append('vin')
# # brick = brick.index(0)
# brick.pop(-3)
# brick.insert(2,9)
# brick.reverse()
#
#
#
# print(brick)
# districts = {'01', '02', '03', '04', '05', '06', '07', '08', '09'}
# print(type(districts))
#
# print(int(312.0 - 2 * 6))
# print(100 if 300 // 2 == 150 else 200)
# g = ['We', 'Are', 'Dumb']
# g.sort()
# g = [i.upper for i in g]
# g = g[::-1]
# print(g)

# kgr = ['1', '2,', '3', '4', '5', '6', '7']
# ft = kgr[::-1]
# print(ft)

# counter = 5
#
# while counter != 0:
#     print('Geeks. Python, first month, final test!')
#     counter -=

import random

question = input('enter your question: ')
emb = random.randint(1, 7)


if emb == 1:
  print('Yes')
elif emb == 2:
  print('No')
elif emb == 3:
    print('Without a doubt')
elif emb == 4:
    print('Ask again later')
elif emb == 5:
    print('Better not to tell you now')
elif emb == 6:
    print('You are a fool if you think so')
else:
  print('he he hehhe')
