def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0

    for i in range(len(number)):
        digit = int(number[i])
        if digit % 2 == 0:
            even_sum += digit
        elif digit % 2 != 0:
            odd_sum += digit
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


current_number = input()
odd_even_sum(current_number)
