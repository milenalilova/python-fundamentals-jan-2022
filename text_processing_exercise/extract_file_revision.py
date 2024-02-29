line = input().split('\\')
data = line[-1].split('.')
file_name = data[0]
file_extension = data[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
