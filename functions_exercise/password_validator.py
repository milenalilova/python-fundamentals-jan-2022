# password = input()
# letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits = '0123456789'
# is_length_valid = False
# is_valid = False
# contains_two_digits = False
# digit_count = 0
# not_letter_or_digit = 0
#
# if 6 <= len(password) <= 10:
#     is_length_valid = True
# else:
#     print('Password must be between 6 and 10 characters')
#
# for i in range(len(password)):
#     if password[i] not in letters and password[i] not in digits:
#         not_letter_or_digit += 1
#         only_digits = True
#     if password[i] in letters:
#         contains_letters = True
#     if password[i] in digits:
#         digit_count += 1
#         contains_digits = True
#
# if not_letter_or_digit > 0:
#     print('Password must consist only of letters and digits')
#
# if digit_count < 2:
#     print('Password must have at least 2 digits')
# else:
#     contains_two_digits = True
#
# if is_length_valid and contains_two_digits and not_letter_or_digit == 0:
#     is_valid = True
#
# if is_valid:
#     print('Password is valid')


# if password.isalnum():
#     print('yes')


def password_validator(pass_word):

    if 6 <= len(pass_word) <= 10:
        pass
    if pass_word.isalnum():
        pass
    if pass_word.isdigit():
        pass


