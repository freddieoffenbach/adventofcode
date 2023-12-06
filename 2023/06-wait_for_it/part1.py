with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

total = 1

times, distances = lines
times = [int(x) for x in times.split(':')[1].split()]
distances = [int(x) for x in distances.split(':')[1].split()]

for idx, t in enumerate(times):
    count = 0
    for h in range(1, t):
        if h * (t - h)  > distances[idx]:
            count += 1
    total *= count

print(total) # 2269432
