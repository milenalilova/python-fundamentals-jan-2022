factor = int(input())
count = int(input())
multiples_list = []
num = 0

for i in range(count):
    num += factor
    multiples_list.append(num)

print(multiples_list)
