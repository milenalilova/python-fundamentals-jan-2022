# def char_in_range(ch1, ch2):
#     for i in range(ord(ch1)+1, ord(ch2)):
#         print(chr(i), end=' ')
#
#
# char_a = input()
# char_b = input()
# char_in_range(char_a, char_b)


def char_in_range(ch1, ch2):
    result = []
    for i in range(ord(ch1) + 1, ord(ch2)):
        result.append(chr(i))
        
    return ' '.join(result)


char_a = input()
char_b = input()
print(char_in_range(char_a, char_b))
