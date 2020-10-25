# 10-3. Guest:

name = input("What's your name? ")

filename = 'chapter_10/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(name)
