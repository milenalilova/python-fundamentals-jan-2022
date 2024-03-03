import re

text = input()

pattern = r"( |^)[a-zA-Z0-9]+(([\.|\_|\-])([a-zA-Z0-9]+))*@[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"

emails = re.finditer(pattern, text)

emails_list = []

for email in emails:
    print(email[0])
