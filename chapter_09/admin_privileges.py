"""A collection of classes for modeling an admin user account."""

from user import User

class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can delete user accounts']

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()