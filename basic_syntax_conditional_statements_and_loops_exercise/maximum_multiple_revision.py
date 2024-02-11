divisor = int(input())
boundary = int(input())
largest_num = 0

for num in range(1, boundary + 1):
    if num % divisor == 0:
        if num > largest_num:
            largest_num = num
print(largest_num)
