with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

total = 1
count = 0

time, distance = lines
time = int(time.split(':')[1].replace(' ', ''))
distance = int(distance.split(':')[1].replace(' ', ''))

for h in range(1, time):
    if h * (time - h)  > distance:
        count += 1
total *= count

print(total) # 35865985
