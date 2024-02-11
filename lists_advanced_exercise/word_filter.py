text = input().split(' ')
even_list = list(word for word in text if len(word) % 2 == 0)

print(' \n'.join(even_list))
