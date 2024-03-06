import re

text = input()
destinations = []
travel_points = 0

pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"

matches = re.finditer(pattern, text)

for match in matches:
    location = match.group(2)
    destinations.append(location)
    travel_points += len(location)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
