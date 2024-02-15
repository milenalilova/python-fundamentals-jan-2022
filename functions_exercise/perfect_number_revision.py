def perfect_number(n):
    sum_divisors = 0

    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i

    if sum_divisors == n:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


current_number = int(input())
perfect_number(current_number)
