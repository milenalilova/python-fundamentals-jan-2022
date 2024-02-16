words = list(input().split(' '))
palindrome = input()
palindrome_words = [word for word in words if word == ''.join(reversed(word))]

result = palindrome_words.count(palindrome)

print(palindrome_words)
print(f"Found palindrome {result} times")
