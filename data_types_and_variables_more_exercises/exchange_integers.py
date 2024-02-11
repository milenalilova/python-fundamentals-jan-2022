# num_one = int(input())
# num_two = int(input())
#
# print('Before:')
# print(f'a = {num_one}')
# print(f'b = {num_two}')
# print('After:')
# print(f'a = {num_two}')
# print(f'b = {num_one}')


a = int(input())
b = int(input())

print('Before:')
print(f'a = {a}')
print(f'b = {b}')

c = a
a = b
b = c

print('After:')
print(f'a = {a}')
print(f'b = {b}')
