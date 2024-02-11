def info():
    countries = input().split(", ")
    capitals = input().split(", ")
    data = dict(zip(countries, capitals))

    for key, value in data.items():
        print(f"{key} -> {value}")


info()
