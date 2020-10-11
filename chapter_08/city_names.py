# 8-6. City Names:
def city_country(city, country):
    """Return a String"""
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)

city = city_country('paris', 'france')
print(city)

city = city_country('moscow', 'russia')
print(city)