num = float(input())

if num == 0:
    print("zero")

elif num > 0:
    if num < 1:
        print("small positive")
    elif num > 100000:
        print("large positive")
    else:
        print("positive")

elif num < 0:
    if abs(num) < 1:
        print("small negative")
    elif abs(num) > 100000:
        print("large negative")
    else:
        print("negative")
