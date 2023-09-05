with open('results.txt') as file:
    lines = file.readlines()

results = {}
for i in lines[1:]:
    name = i.split()[0]
    rate = i.split()[1]
    results[name] = {"rate": int(rate)}

sorted_results = sorted(results.items(), key=lambda x: x[1]['rate'], reverse=True)

print('top 3 students')
for i, (name, result) in enumerate(sorted_results[:3], 1):
    print(f'{i}. {name}: {result["rate"]}')

with open('sorted_results.txt', 'w') as file:
    file.write('results\n')
    for name, result in sorted_results:
        file.write(f'name: {name}  rate: {result["rate"]}\n')

with open('sorted_results.txt') as file:
    print(f'sorted_results.txt:\n{file.read()}')