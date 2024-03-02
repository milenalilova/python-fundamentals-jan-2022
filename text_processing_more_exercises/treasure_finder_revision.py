keys = [int(x) for x in input().split(' ')]
line = input()

while line != "find":
    new_line = ''
    for i in range(len(line)):
        new_line += chr(ord(line[i]) - keys[i % len(keys)])
    type = new_line.split('&')[-2]
    coordinates = new_line.split('<')[-1][:-1]
    print(f"Found {type} at {coordinates}")

    line = input()


# Better version
# secret_key = [int(x) for x in input().split()]
# secret_msg = input()
#
# how_long = len(secret_key)
# while secret_msg != "find":
#     secret_text = "".join([chr(ord(secret_msg[i]) - secret_key[i % how_long]) for i in range(len(secret_msg))])
#     item = secret_text.split("&")[-2]
#     location = secret_text.split("<")[-1][:-1]
#     print(f"Found {item} at {location}")
#     secret_msg = input()
