number = int(input())
is_prime = True

if number > 1:
    for a in range(1, number):
        for b in range(1, number):
            result = a * b
            if result == number:
                is_prime = False
                break
        if not is_prime:
            break

print(is_prime)
