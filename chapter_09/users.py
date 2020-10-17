# 9-3. Users:
class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.username = username

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

elon = User('elon', 'musk', '@elonmusk', 'elonmusk@gmail.com')
elon.describe_user()
elon.greet_user()

donald = User('donald', 'trump', '@realDonaldTrump', 'donaldtrump@gmail.com')
donald.describe_user()
donald.greet_user()