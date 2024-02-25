n = int(input())
synonyms_dict = {}

for line in range(n):
    word = input()
    synonym = input()
    if word not in synonyms_dict.keys():
        synonyms_dict[word] = []
    synonyms_dict[word].append(synonym)

for k, v in synonyms_dict.items():
    print(f"{k} - {', '.join(v)}")
