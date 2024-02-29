first_str, second_str = input().split()

length = min(len(first_str), len(second_str))

sum_chars = 0

for i in range(length):
    sum_chars += ord(first_str[i]) * ord(second_str[i])

if len(first_str) > length:
    for i in range(length, len(first_str)):
        sum_chars += ord(first_str[i])
elif len(second_str) > length:
    for i in range(length, len(second_str)):
        sum_chars += ord(second_str[i])

print(sum_chars)
