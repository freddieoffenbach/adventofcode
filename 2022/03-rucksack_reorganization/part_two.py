with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw'
]

sum = 0
types = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
priorites = []
for n in range(1, 53):
    priorites.append(n)
items = dict(zip(types, priorites))

for line in lines:
    x = int(len(line) / 2)
    comp1 = line[:x]
    comp2 = line[x:]
    for c in comp1:
        if c in comp2:
            sum += items[c]
            break

print(sum) # 7763
