# 3-8. Seeing the World:
places = ['Patagonia', 'New York', 'New Zealand', 'British Columbia', 'Portugal']
print(places)

# sorted in alphabetical order
print(sorted(places))

# sorted in reversed alphabetical order
print(sorted(places, reverse=True))

# in reversed order
places.reverse()
print(places)

# in original order
places.reverse()
print(places)

# sorted in alphabetical order
places.sort()
print(places)

# sorted in reversed alphabetical order
places.sort(reverse=True)
print(places)


# 3-9. Dinner Guests:
guest_list = ['Neil deGrasse Tyson', 'Richard Dawkins', 'Alan Turing']
print(f'We invited {len(guest_list)} guests.')
