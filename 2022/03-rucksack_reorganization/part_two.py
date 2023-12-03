with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0

for x in range(0, len(lines), 3):
    for c in lines[x]:
        if c in lines[x + 1] and c in lines[x + 2]:
            if c.islower():
                sum += ord(c) - 96
            else:
                sum += ord(c) - 38
            break

print(sum) # 2569
