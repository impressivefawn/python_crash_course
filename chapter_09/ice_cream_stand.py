# 9-6. Ice Cream Stand:
class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.restaurant_name.title()} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        """Display a message if a restaurant is open."""
        print(f"{self.restaurant_name.title()} is open. Come on in!")

class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'green tea', 'pistachio', 'wintergreen']

    def display_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

gelato_scoops = IceCreamStand('gelato scoops')
gelato_scoops.describe_restaurant()
gelato_scoops.display_flavors()