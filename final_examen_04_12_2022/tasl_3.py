line = input().split('|')
notebook = {}

for item in line:
    data = item.split(':')
    word = data[0].strip()
    definition = data[1].strip()

    if word not in notebook.keys():
        notebook[word] = []
    notebook[word].append(definition)

words = input().split('|')

command = input()

if command == 'Test':
    for el in words:
        el = el.strip()
        if el in notebook:
            if el in notebook:
                result = f'{el}:\n'
                result += ' -'
                result += f'\n -'.join(notebook[el])
                print(result.strip())

if command == 'Hand Over':
    result = ' '.join(notebook)
    print(result)
