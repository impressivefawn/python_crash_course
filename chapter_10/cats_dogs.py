# 10-8. Cats and Dogs:
filenames = ['cats.txt', 'chapter_10/dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")
    else:
        print(contents.title())



