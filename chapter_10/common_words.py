# 10-10. Common Words:

books = ['chapter_10/prince.txt', 'chapter_10/moby_dick.txt', 'chapter_10/frankenstein.txt']

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        message = print(f"The word '{word}' appears about {word_count} times in {filename}.")


for book in books:
    count_common_words(book, 'you')

