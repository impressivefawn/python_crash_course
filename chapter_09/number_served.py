# 9-4. Number Served:
class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.restaurant_name.title()} offers the best dishes of {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        """Display a message if a restaurant is open."""
        print(f"{self.restaurant_name.title()} is open. Come on in!")

    def set_number_served(self, number):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, increment):
        """Allow user to increment the number of customers served."""
        self.number_served += increment

restaurant = Restaurant('palermo', 'italian')
print(f"\nNumber served: {restaurant.number_served}")

restaurant.number_served = 5
print(f"\nNumber served: {restaurant.number_served}")

restaurant.set_number_served(7)
print(f"\nNumber served: {restaurant.number_served}")

restaurant.increment_number_served(53)
print(f"\nNumber served: {restaurant.number_served}")