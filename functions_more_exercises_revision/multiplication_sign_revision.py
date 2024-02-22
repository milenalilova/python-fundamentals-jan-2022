def get_result(num_one, num_two, num_three):
    negatives = 0
    result = ''

    if num_one == 0 or num_two == 0 or num_three == 0:
        result = 'zero'
    else:
        if num_one < 0:
            negatives += 1
        if num_two < 0:
            negatives += 1
        if num_three < 0:
            negatives += 1

        if negatives % 2 != 0:
            result = 'negative'
        else:
            result = 'positive'

    return result


current_num_one = int(input())
current_num_two = int(input())
current_num_three = int(input())

print(get_result(current_num_one, current_num_two, current_num_three))
