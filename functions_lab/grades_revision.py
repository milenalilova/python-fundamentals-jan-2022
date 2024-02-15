def print_grades(grade):
    if grade < 3:
        print('Fail')

    elif grade < 3.50:
        print('Poor')

    elif grade < 4.50:
        print('Good')

    elif grade < 5.50:
        print('Very Good')

    elif grade < 6:
        print('Excellent')


current_grade = float(input())
print_grades(current_grade)
