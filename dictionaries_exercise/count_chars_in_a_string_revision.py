line = [char for char in input() if char != ' ']
chars_dict = {}

for ch in line:
    if ch not in chars_dict.keys():
        chars_dict[ch] = 0
    chars_dict[ch] += 1

for k, v in chars_dict.items():
    print(f"{k} -> {v}", end='\n')
