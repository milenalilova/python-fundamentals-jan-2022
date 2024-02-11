# # tail = input()
# # body = input()
# # head = input()
# #
# # meerkat = [head, body, tail]
# #
# # print(meerkat)
#
#
# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
#
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
#
# print(meerkat)


# tail = input()
# body = input()
# head = input()
#
# meerkat = [head, body, tail]
#
# print(meerkat)


# tail = input()
# body = input()
# head = input()
#
# list = [head, body, tail]
#
# print(list)


# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
#
# temp = meerkat[0]
# meerkat[0] = meerkat[2]
# meerkat[2] = temp
#
# print(meerkat)


meerkat = []   # meerkat = list()

meerkat.append(input())
meerkat.append(input())
meerkat.append(input())

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)
