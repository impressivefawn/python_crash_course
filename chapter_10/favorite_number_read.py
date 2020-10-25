import json

filename = 'chapter_10/favorite_number.json'

with open(filename) as f:
    number = json.load(f)

print(f"I know your favorite number! It's {number}.")