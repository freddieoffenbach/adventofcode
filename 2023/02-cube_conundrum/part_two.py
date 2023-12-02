with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

sum = 0

for line in lines:
    minimum = 1
    bag = {}
    id, sets = line[5:].split(':')
    sets = sets.split(';')
    for set in sets:
        cubes = set.split(',')
        for cube in cubes:
            n, color = (cube.split())
            bag_n = bag.get(color)
            if bag_n is None:
                bag_n = 0
            bag[color] = max(int(n), bag_n)
    for n in bag.values():
        minimum *= n
    sum += minimum

print(sum) # 63542
