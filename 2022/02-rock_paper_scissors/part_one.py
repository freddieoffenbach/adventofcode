with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

total = 0

scores = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6
}

for line in lines:
    total += scores[line]

print(total) # 13268
