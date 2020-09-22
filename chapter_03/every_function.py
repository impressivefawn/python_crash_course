# 3-10. Every Function:
largest_cities = ['Delhi', 'Shanghai', 'São Paulo', 'Mexico City']

# Accessing Elements in a List
print(largest_cities[0])

# Appending Elements to the End of a List
largest_cities.append('Cairo')
largest_cities.append('Mumbai')
print(largest_cities)

# Inserting Elements into a List
largest_cities.insert(0, 'Tokyo')
print(largest_cities)

# Removing an Item Using the pop() Method
largest_cities.pop()
print(largest_cities)

# Removing an Item by Value
largest_cities.remove('Cairo')
print(largest_cities)

# Sorted in alphabetical order
print(sorted(largest_cities))

# Sorting in reversed order
largest_cities.reverse()
print(largest_cities)

# Back to original order
largest_cities.reverse()
print(largest_cities)

# Finding the Length of a List
print(len(largest_cities))

# Sorting a List Permanently
largest_cities.sort()
print(largest_cities)

# Sorting a List Permanently in reversed order
largest_cities.sort(reverse=True)
print(largest_cities)