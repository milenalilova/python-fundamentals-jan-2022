sequence_list = input().split(' ')
abs_list = []

for num in sequence_list:
    abs_list.append(abs(float(num)))

print(abs_list)
