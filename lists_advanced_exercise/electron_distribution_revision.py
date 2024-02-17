def fill_shells(electrons_count):
    shells = []
    counter = 1

    while electrons_count > 0:
        electrons = 2 * (counter ** 2)
        if electrons < electrons_count:
            shells.append(electrons)
            electrons_count -= electrons
        else:
            shells.append(electrons_count)
            electrons_count = 0

        counter += 1

    print(shells)


current_electrons_count = int(input())
fill_shells(current_electrons_count)



# Variant 2
# electrons_count = int(input())
# shells = []
# counter = 1
#
# while electrons_count > 0:
#     result = 2 * (counter ** 2)
#     if result < electrons_count:
#         shells.append(result)
#         electrons_count -= result
#     else:
#         shells.append(electrons_count)
#         electrons_count -= electrons_count
#     counter += 1
#
# print(shells)
