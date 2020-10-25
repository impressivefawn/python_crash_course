# 10-12. Favorite Number Remembered:
import json

filename = 'chapter_10/favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        number = input("What's your favorite number? ")
        json.dump(number, f)
    print("Thanks! I'll remember that.")
else:
    print(f"I know your favorite number! It's {number}.")