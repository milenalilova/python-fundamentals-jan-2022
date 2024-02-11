def palindrome(number):
    for num in number:
        if num == num[::-1]:
            print('True')
        else:
            print('False')


current_num = input().split(', ')
palindrome(current_num)
