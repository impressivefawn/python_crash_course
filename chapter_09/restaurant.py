# 9-1. Restaurant:
class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.restaurant_name.title()} offers the best dishes of {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        """Display a message if a restaurant is open."""
        print(f"{self.restaurant_name.title()} is open. Come on in!")