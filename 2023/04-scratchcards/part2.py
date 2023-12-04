with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

total = 0
cards = [1] * len(lines)

for idx, line in enumerate(lines):
    win_nums, nums = line[line.index(':') + 1:].split('|')
    win_nums = set(win_nums.split())
    nums = set(nums.split())
    match_cnt = len(win_nums.intersection(nums))

    for copy in range(match_cnt):
        cards[idx + copy + 1] += cards[idx]

total = sum(cards)

print(total) # 5554894
