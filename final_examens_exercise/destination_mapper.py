import re

text = input()
pattern = r'([=\/])[A-Z][a-zA-Z]{2,}\1'

destinations = re.finditer(pattern, text)
countries = []
travel_points = 0

for country in destinations:
    countries.append(country[0][1:-1])
    travel_points += len(country[0][1:-1])

print(f"Destinations: {', '.join(countries)}")
print(f'Travel Points: {travel_points}')
