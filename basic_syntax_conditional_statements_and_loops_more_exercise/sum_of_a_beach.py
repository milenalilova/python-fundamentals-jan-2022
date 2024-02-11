text = input()
text = text.lower()
searched_list = ["sand", "water", "fish", "sun"]
sum = 0

for element in searched_list:
    if element in text:
        element_count = text.count(element)
        sum += element_count

print(sum)
