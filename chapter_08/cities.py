# 8-5. Cities:
def describe_city(city, country='spain'):
    """Describe a city."""
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('Madrid')
describe_city(city='Buenos Aires', country='Argentina')
describe_city('punta arenas', 'chile')