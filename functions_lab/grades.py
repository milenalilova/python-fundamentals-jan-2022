# def grade_text():
#     grade = float(input())
#
#     if grade < 3:
#         return "Fail"
#     elif grade < 3.5:
#         return "Poor"
#     elif grade < 4.5:
#         return "Good"
#     elif grade < 5.5:
#         return "Very Good"
#     else:
#         return "Excellent"
#
#
# print(grade_text())


def grade_text(grade_number):

    if grade_number < 3:
        return "Fail"
    elif grade_number < 3.5:
        return "Poor"
    elif grade_number < 4.5:
        return "Good"
    elif grade_number < 5.5:
        return "Very Good"
    else:
        return "Excellent"


current_grade = float(input())

print(grade_text(current_grade))
print(grade_text(5))
print(grade_text(3.33))
print(grade_text(4.6))

