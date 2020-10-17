# 9-5. Login Attempts:
class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


elon = User('elon', 'musk', '@elonmusk', 'elonmusk@gmail.com')
elon.describe_user()
elon.greet_user()

print("\nMaking 3 login attempts...")
elon.increment_login_attempts()
elon.increment_login_attempts()
elon.increment_login_attempts()
print(f"  Login attempts: {elon.login_attempts}")

elon.reset_login_attempts()
print("\nLogin attempts reset.")
print(f"Login attempts: {elon.login_attempts}")