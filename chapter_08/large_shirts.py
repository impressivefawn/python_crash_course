# 8-4. Large Shirts:
def make_shirt(size='large', message='love Python'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')


make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='I love NY')