usernames = input().split(', ')

for username in usernames:
    is_valid = True

    if not 3 <= len(username) <= 16:
        is_valid = False

    for ch in username:
        if not ch.isalpha() and not ch.isdigit() and ch != '-' and ch != '_':
            is_valid = False

    if is_valid:
        print(username)
