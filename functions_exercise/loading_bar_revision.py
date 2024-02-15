def loading_bar(num):
    n = num // 10
    result = f"{n * '%'}{(10 - n) * '.'}"
    if num != 100:
        print(f"{num}% [{result}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


current_num = int(input())
loading_bar(current_num)
