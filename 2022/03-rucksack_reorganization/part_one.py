with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0

for line in lines:
    x = len(line) // 2
    for c in line[:x]:
        if c in line[x:]:
            if c.islower():
                sum += ord(c) - 96
            else:
                sum += ord(c) - 38
            break

print(sum) # 7763
