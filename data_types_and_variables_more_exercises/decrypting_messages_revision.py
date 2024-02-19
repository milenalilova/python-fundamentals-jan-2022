key = int(input())
n = int(input())
word = ''

for i in range(n):
    char = input()
    word += chr(ord(char) + key)

print(word)
