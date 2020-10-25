# 10-11. Favorite Number:
import json

filename = 'chapter_10/favorite_number.json'

number = input("What's your favorite number? ")

with open(filename, 'w') as f:
    json.dump(number, f)
    print("Thanks! I'll remember that.")