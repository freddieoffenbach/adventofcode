with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

sum = 0

for line in lines:
    min = 1
    bag = {'red': 0, 'green': 0, 'blue': 0}
    id, sets = line[5:].split(':')
    for set in sets.split(';'):
        for cube in set.split(','):
            n, c = cube.split()
            b = bag.get(c)
            bag[c] = max(int(n), b)
    for n in bag.values():
        min *= n
    sum += min

print(sum) # 63542
