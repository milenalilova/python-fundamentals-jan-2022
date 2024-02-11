# words = input().split(' ')
# palindrome = input()
# palindrome_list = []
#
# for word in words:
#     if word == word[::-1]:
#         palindrome_list.append(word)
#
# print(palindrome_list)
# print(f'Found palindrome {words.count(palindrome)} times')


words = input().split(' ')
palindrome = input()
palindrome_list = []

for word in words:
    rev_list = reversed(word)
    rev_word = ''.join(rev_list)
    if rev_word == word:
        palindrome_list.append(word)

print(palindrome_list)
print(f'Found palindrome {words.count(palindrome)} times')
