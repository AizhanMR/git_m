with open('new_file.txt', 'r') as file:
    # print(file.read())
    print(file.readlines()[2])
    print(file.read())

# file = open('new_file.txt', 'w')
# file.write('Бишкек, Кыргызстан')
# file.close()


# with open('new_file.txt', 'a') as file:
#     file.write('\nтретья строка! ')


# with open('file.txt', 'x') as new_file:
#     new_file.write('new file')