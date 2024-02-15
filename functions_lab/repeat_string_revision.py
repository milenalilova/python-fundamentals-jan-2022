def repeat_string(string, counter):
    new_string = string * counter
    return new_string


current_string = input()
current_counter = int(input())

print(repeat_string(current_string, current_counter))



# Variant 2
# repeater = lambda string, n: string * n

# current_string = input()
# current_n = int(input())

# print(repeater(current_string, current_n))
