import re

participants = input().split(', ')
info = input()
scores_dict = {}

letters_pattern = r"[a-zA-Z]+"
digits_pattern = r"\d"

while info != "end of race":

    letters_matches = re.findall(letters_pattern, info)
    digits_matches = re.findall(digits_pattern, info)
    digits_matches = [int(num) for num in digits_matches]

    name = ''.join(letters_matches)
    distance = sum(digits_matches)

    if name in participants:
        if name not in scores_dict:
            scores_dict[name] = distance
        else:
            scores_dict[name] += distance

    info = input()

sorted_scores = sorted(scores_dict.items(), key=lambda x: x[1], reverse=True)

print(f"1st place: {sorted_scores[0][0]}")
print(f"2nd place: {sorted_scores[1][0]}")
print(f"3rd place: {sorted_scores[2][0]}")
