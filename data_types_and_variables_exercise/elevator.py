number_people = int(input())
capacity = int(input())
course_counter = 0

while number_people > 0:
    number_people -= capacity
    course_counter += 1

print(course_counter)


# import math
#
# number_people = int(input())
# capacity = int(input())
#
# courses = math.ceil(number_people / capacity)
#
# print(courses)


# number_people = int(input())
# capacity = int(input())
#
# courses = number_people / capacity
# if number_people % capacity == 0:
#     print(int(courses))
# else:
#     print(int(courses) + 1)
