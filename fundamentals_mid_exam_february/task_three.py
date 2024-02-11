price_ratings = list(map(int, input().split(', ')))
entry_point = int(input())
type_item = input()

left_sum = 0
right_sum = 0

left_items = price_ratings[:entry_point]
right_items = price_ratings[entry_point + 1:]

if type_item == 'cheap':
    for item in left_items:
        if item < price_ratings[entry_point]:
            left_sum += item
    for item in right_items:
        if item < price_ratings[entry_point]:
            right_sum += item

elif type_item == 'expensive':
    for item in left_items:
        if item >= price_ratings[entry_point]:
            left_sum += item
    for item in right_items:
        if item >= price_ratings[entry_point]:
            right_sum += item

if left_sum > right_sum:
    print(f' Left - {left_sum}')

elif left_sum < right_sum:
    print(f'Right - {right_sum}')

elif left_sum == right_sum:
    print(f'Left - {left_sum}')
