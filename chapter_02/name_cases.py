name = 'Adventurer'
print(f'Hello {name} and welcome to the Town of Honeywood!')

print(f'Hello {name.lower()} and welcome to the Town of Honeywood!')
print(f'Hello {name.upper()} and welcome to the Town of Honeywood!')
print(f'Hello {name.title()} and welcome to the Town of Honeywood!')

# Write a quote 
author = 'Baelin the Fisherman'
quote = "Nice day for fishing ain't it?"
message = f'{author} once said, "{quote}"'
print(message)

# Print name using the three stripping functions
name = ' High \nSorcerer \tBaradun '
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())