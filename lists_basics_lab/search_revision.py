n = int(input())
word = input()
word_list = []

for i in range(n):
    string = input()
    word_list.append(string)

print(word_list)

for i in range(len(word_list)-1, -1, -1):
    if word not in word_list[i]:
        word_list.remove(word_list[i])

print(word_list)
