lines_num = int(input())
total_sum = 0

for ch in range(lines_num):
    char = input()
    total_sum += ord(char)

print(f"The sum equals: {total_sum}")
