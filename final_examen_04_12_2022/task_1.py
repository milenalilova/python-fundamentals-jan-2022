# Hogwarts

spell_to_be_deciphered = input()
instruction = input()
commands_list = ['Abjuration', 'Necromancy', 'Illusion', 'Divination', 'Alteration']

while instruction != 'Abracadabra':
    data = instruction.split(' ')
    command = data[0]

    if command not in commands_list:
        print('The spell did not work!')

    if command == 'Abjuration':
        spell_to_be_deciphered = spell_to_be_deciphered.upper()
        print(spell_to_be_deciphered)

    elif command == 'Necromancy':
        spell_to_be_deciphered = spell_to_be_deciphered.lower()
        print(spell_to_be_deciphered)

    elif command == 'Illusion':
        idx = int(data[1])
        letter = data[2]

        if idx < 0 or idx >= len(spell_to_be_deciphered):
            print('The spell was too weak.')

        else:
            spell_to_be_deciphered = spell_to_be_deciphered[0:idx] + letter + spell_to_be_deciphered[idx + 1:]
            print('Done!')

    elif command == 'Divination':
        first_substring = data[1]
        second_substring = data[2]
        if first_substring not in spell_to_be_deciphered:
            pass
        else:
            spell_to_be_deciphered = spell_to_be_deciphered.replace(first_substring, second_substring)
            print(spell_to_be_deciphered)

    elif command == 'Alteration':
        substring = data[1]

        if substring not in spell_to_be_deciphered:
            pass

        else:
            spell_to_be_deciphered = spell_to_be_deciphered.replace(substring, '')
            print(spell_to_be_deciphered)

    # elif command not in commands_list:
    #     print('The spell did not work!')

    instruction = input()
