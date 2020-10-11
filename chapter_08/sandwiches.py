# 8-12. Sandwiches:
def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('cheese')
make_sandwich('cheese', 'tuna')
make_sandwich('cheese', 'tuna', 'extra chicken')