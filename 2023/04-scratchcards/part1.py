with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

total = 0

for line in lines:
    win_nums, nums = line[line.index(':') + 1:].split('|')
    win_nums = set(win_nums.split())
    nums = set(nums.split())
    match_cnt = len(win_nums.intersection(nums))
    if match_cnt > 0:
        total += 2 ** (match_cnt - 1)

print(total) # 17803
