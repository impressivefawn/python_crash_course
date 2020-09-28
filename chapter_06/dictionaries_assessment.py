# 6-7. People:
people = [
    {'first_name': 'Donald ', 'last_name': 'Trump', 'age': 74, 'city': 'Washington D.C'},
    {'first_name': 'Barack ', 'last_name': 'Obama', 'age': 59, 'city': 'Washington D.C'},
    {'first_name': 'George', 'last_name': 'Bush', 'age': 74, 'city': 'Prairie Chapel Ranch'},
    ]

for person in people:
    print(f"{person['first_name']} {person['last_name']} is {person['age']} years old. He resides in {person['city']}.")

# 6-8. Pets:
pets = [
    {'kind': 'cat', 'name': 'peach', 'eats': 'mice'},
    {'kind': 'dog', 'name': 'daisy', 'eats': 'watermelons'},
    {'kind': 'fish', 'name': 'guppy', 'eats': 'worms'},
    ]

print("")
for pet in pets:
    print(f"{pet['name'].title()} is a nice {pet['kind']}. {pet['name'].title()} loves eating {pet['eats']}.")

# 6-9. Favorite Places:
favorite_places = {
    'kate': ['paris', 'alaska'],
    'pete': ['yosemite'], 
    'boris': ['caucasus', 'altai'],
    'veronika': ['melbourne', 'aukland'],
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f" - {place.title()}")

# 6-10. Favorite Numbers:
import random
favorite_numbers = {
    'kate': [random.randint(1, 10), random.randint(1, 10)],
    'pete': [random.randint(1, 10)], 
    'boris': [random.randint(1, 10)],
    'veronika': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"  {number}")

# 6-11. Cities:
cities = {
    'sydney': {'country': 'australia', 'population': 5.23, 'fact': 'The cost of building the Sydney Opera House ended up at $102 million instead of the original estimate of $7 million.'},
    'buenos aires': {'country': 'argentina', 'population': 2.89, 'fact': 'Very similar to Washington D.C., Buenos Aires is its own federal district where the president of the country lives.'},
    'los angeles': {'country': 'united states', 'population': 3.99, 'fact': 'When LA was founded, the city’s full name was "El Pueblo de Nuestra Senora Reina de los Angeles sobre el Rio Porciuncula".'},
}

for city, city_info in cities.items():
    print(f"\n{city.title()} is located in {city_info['country'].title()}.")
    print(f"  It has a population of about {city_info['population']} million people.")
    print(f"  Fact: {city_info['fact']}")

