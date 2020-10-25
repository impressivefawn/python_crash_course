# 10-9. Silent Cats and Dogs:
filenames = ['chapter_10/cats.txt', 'dogs.txt']

for filename in filenames:

    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents.title())
