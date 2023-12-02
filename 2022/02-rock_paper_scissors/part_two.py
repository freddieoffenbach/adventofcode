with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

total = 0

scores = {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7
}

for line in lines:
    total += scores[line]

print(total) # 15508
