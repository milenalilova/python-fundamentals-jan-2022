times = list(map(int, input().split(' ')))
finish_line = len(times) // 2
sum_times = sum(times)

time_first = 0
time_second = 0

for i in range(finish_line):
    if times[i] == 0:
        time_first -= time_first * 0.2
    time_first += times[i]

for j in range(len(times) - 1, finish_line, -1):
    if times[j] == 0:
        time_second -= time_second * 0.2
    time_second += times[j]

if time_first < time_second:
    print(f"The winner is left with total time: {time_first:.1f}")
else:
    print(f"The winner is right with total time: {time_second:.1f}")
