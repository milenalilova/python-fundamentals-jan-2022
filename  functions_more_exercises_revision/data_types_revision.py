def data_type(string, object):
    result = 0
    if string == "int":
        result = int(object) * 2

    elif string == "real":
        result = f"{float(object) * 1.5:.2f}"

    elif string == "string":
        result = f"${object}$ "

    return result


current_string = input()
current_object = input()
print(data_type(current_string, current_object))
