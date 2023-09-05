ten = list(range(1, 11))
print(ten)

evens = list(filter(lambda num: num % 2 == 0, ten))
print(evens)

square = list(map(lambda num: num ** 2, evens))
print(square)

def get_index(lst=ten):
    while True:
        try:
            index = input('Enter index or "exit" to finish')
            if index == 'exit':
                print('Finish')
                break
            print(lst[int(index)])
        except:
            print(f'Enter numbers only from 0 to {len(lst) - 1}')
print(get_index(ten))