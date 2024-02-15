def password_validator(password):
    is_valid = False
    is_correct_length = False
    is_alphanum = True
    has_two_nums = False

    if 6 <= len(password) <= 10:
        is_correct_length = True

    for ch in password:
        if not ch.isalnum():
            is_alphanum = False
            break

    numerics = 0
    for ch in password:

        if ch.isdigit():
            numerics += 1
        if numerics >= 2:
            has_two_nums = True

    if not is_alphanum:
        print("Password must consist only of letters and digits")

    if not is_correct_length:
        print("Password must be between 6 and 10 characters")

    if not has_two_nums:
        print("Password must have at least 2 digits")

    if is_correct_length and is_alphanum and has_two_nums:
        is_valid = True

    if is_valid:
        print("Password is valid")


current_password = input()
password_validator(current_password)
