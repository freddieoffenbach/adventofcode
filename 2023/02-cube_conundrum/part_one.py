with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

sum = 0
bag = {'red': 12, 'green': 13, 'blue': 14}

for line in lines:
    is_possible = True
    id, sets = line[5:].split(':')
    sets = sets.split(';')
    for set in sets:
        cubes = set.split(',')
        for cube in cubes:
            n, color = (cube.split())
            if int(n) > bag.get(color):
                is_possible = False
    if is_possible:
        sum += int(id)

print(sum) # 2268
