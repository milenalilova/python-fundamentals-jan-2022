countries = input().split(', ')
capitals = input().split(', ')
info = dict(zip(countries, capitals))

for k, v in info.items():
    print(f"{k} -> {v}")
