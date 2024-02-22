def get_first_tribonacci_numebrs(n: int):
    tribonacci_sequence = [0, 0, 1]

    for i in range(n):
        next_num = tribonacci_sequence[-1] + tribonacci_sequence[-2] + tribonacci_sequence[-3]
        tribonacci_sequence.append(next_num)

    tribonacci_sequence = [num for num in tribonacci_sequence if num != 0]
    tribonacci_sequence = tribonacci_sequence[:n]

    for i in range(len(tribonacci_sequence)):
        print(tribonacci_sequence[i], end=' ')


number = int(input())
get_first_tribonacci_numebrs(number)
