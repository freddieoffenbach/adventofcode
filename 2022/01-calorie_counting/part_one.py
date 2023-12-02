with open('input.txt', 'r') as file:
    lines = file.read().split('\n\n')

total = 0
elves = []

for line in lines:
    cals = 0
    foods = line.split()
    for food in foods:
        cals += int(food)
    elves.append(cals)

total = max(elves)

print(total) # 71934
