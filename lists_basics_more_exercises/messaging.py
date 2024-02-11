sequence_of_numbers = input().split(' ')
text = input()
copy_text = text

sum_of_digits = 0
# message = [0] * len(sequence_of_numbers)
message = []
final_message = ''

for num in sequence_of_numbers:
    for digit in range(len(num)):
        sum_of_digits += int(num[digit])
    message.append(sum_of_digits)
    sum_of_digits = 0

for n in message:
    if n > len(text) - 1:
        index = n % len(text)
    else:
        index = n
    final_message += text[index]
    text = text.replace(text[index], '', 1)

print(final_message)

