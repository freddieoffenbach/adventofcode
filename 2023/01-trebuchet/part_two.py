with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

sum = 0
nums = {'1': 'one', '2': 'two', '3': 'three',
        '4': 'four', '5': 'five', '6': 'six',
        '7': 'seven', '8': 'eight', '9': 'nine'}

for line in lines:
    digits = []
    for x in range(len(line)):
        if line[x].isdigit():
            digits.append(line[x])
        else:
            for n, word in nums.items():
                if line[x:x + len(word)] == word:
                    digits.append(n)
    sum += int(digits[0] + digits[-1])

print(sum) # 55358
