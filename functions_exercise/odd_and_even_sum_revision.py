def odd_and_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for i in range(len(number)):
        num = int(number[i])
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


current_num = input()
print(odd_and_even_sum(current_num))
