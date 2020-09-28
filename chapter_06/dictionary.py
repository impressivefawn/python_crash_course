# 6-1. Person:
person = {'first_name': 'Donald ', 'last_name': 'Trump', 'age': 74, 'city': 'Washington D.C.'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2. Favorite Numbers:
favorite_numbers = {
    'John': 5,
    'Michael': 19,
    'Tyrone': 7,
    'Richard': 13,
    'Boris': 1,
}
print(f"\nJohn's favorite number is {favorite_numbers['John']}.")
print(f"Michael's favorite number is {favorite_numbers['Michael']}.")
print(f"Tyrone's favorite number is {favorite_numbers['Tyrone']}.")
print(f"Richard's favorite number is {favorite_numbers['Richard']}.")
print(f"Boris's favorite number is {favorite_numbers['Boris']}.")

# 6-3. Glossary:
glossary = {
    'list comprehension': 'A list comprehension is a syntactic construct available in some programming languages for creating a list based on existing lists.',
    'tuple': 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in).',
    'f-string': 'F-strings provide a way to embed expressions inside string literals, using a minimal syntax. It should be noted that an f-string is really an expression evaluated at run time, not a constant value.',
    'concatenate': 'to link together in a series or chain',
    'list': 'List is a collection which is ordered and changeable. Allows duplicate members.',
    'set': 'A set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets.',
    'for loop': 'A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.',
    'integer': 'An integer (from the Latin integer meaning "whole") is colloquially defined as a number that can be written without a fractional component.',
    'declaration': 'A declaration of a variable is where a program says that it needs a variable. Unlike other programming languages, Python has no command for declaring a variable.',
}
print("\nGlossary 1")
print(f"List comprehension:\n    {glossary['list comprehension']}")
print(f"Tuple:\n    {glossary['tuple']}")
print(f"F-string:\n    {glossary['f-string']}")
print(f"Concatenate:\n    {glossary['concatenate']}")
print(f"List:\n    {glossary['list']}\n")

# 6-4. Glossary 2:
print("Glossary 2")
for key, value in glossary.items():
    print(f"{key.title()}:\n    {value}")

# 6-5. Rivers:
rivers = {
    'nile': 'egipt',
    'amazon': 'brazil',
    'yangtze': 'china',
}


for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nList of rivers in a dictionary.")
for river in rivers.keys():
    print(river.title())

print("\nList of countries in a dictionary.")
for country in rivers.values():
    print(country.title())

# 6-6. Polling:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

participants = ['edward', 'pete', 'kate', 'annie', 'phil']

for participant in participants:
    if participant in favorite_languages.keys():
        print(f"{participant.title()}, thank you for taking the poll.")
    else:
        print(f"{participant.title()}, you're invited to take a poll.")