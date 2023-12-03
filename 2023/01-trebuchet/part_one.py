with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

sum = 0

for line in lines:
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)
    sum += int(digits[0] + digits[-1])

print(sum) # 56042
