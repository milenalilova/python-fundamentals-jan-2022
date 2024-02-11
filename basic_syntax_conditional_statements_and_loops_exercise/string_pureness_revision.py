n = int(input())

for i in range(n):
    string = input()
    for ch in range(len(string)):
        if string[ch] == "," or string[ch] == "." or string[ch] == "_":
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")
