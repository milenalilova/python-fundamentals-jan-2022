josephus_prisoners = list(map(int, input().split(' ')))
k = int(input())
index = (k - 1) % len(josephus_prisoners)

executed = []

while len(josephus_prisoners) > 1:
    prisoner = josephus_prisoners.pop(index)
    executed.append(prisoner)
    index = (index + k - 1) % len(josephus_prisoners)

executed.extend(josephus_prisoners)

print(str(executed).replace(' ', ''))



# Variant 2
# circle = input().split(' ')
# kill_count = int(input())
# result = []
# counter = 0

# index = 0
# while len(circle) > 0:
#     counter += 1
#
#     if counter % kill_count == 0:
#         result.append(circle.pop(index))
#     else:
#         index += 1
#
#     if index >= len(circle):
#         index = 0
#
# print(str(result).replace(' ', '').replace('\'', ''))