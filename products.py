"""
This module defines the Product class, which represents a product in the store.
"""
class Product:
    """
    Represents a product with a name, price, quantity, and active status.
    """
    total_items_count = 0

    def __init__(self, name, price, quantity, active=True):
        """
        Initializes a new product.
        Checks for valid input types and values.
        """

        if not isinstance(name, str):
            raise TypeError("Product name must be a string text.")
        if len(name.strip()) == 0:
            raise ValueError("Product name cannot be empty or just spaces.")

        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number (integer or float).")
        if price < 0:
            raise ValueError("Price cannot be a negative value.")

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a whole integer number.")
        if quantity < 0:
            raise ValueError("Quantity cannot be a negative value.")

        if not isinstance(active, bool):
            raise TypeError("Active status must be a boolean value (True or False).")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active
        Product.total_items_count += 1

    def get_quantity(self):
        """
        Returns the current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Updates the product quantity.
        """
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a whole integer number.")
        if quantity < 0:
            raise ValueError("Quantity cannot be a negative value.")
        self.quantity = quantity

    def is_active(self):
        """
        Returns True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Sets the product status to active.
        """
        self.active = True

    def deactivate(self):
        """
        Sets the product status to inactive.
        """
        self.active = False

    def show(self):
        """
        Prints the product details.
        """
        print(f"Product name: {self.name}, Price {self.price}, Quantity {self.quantity}")

    def buy(self, quantity):
        """
        Processes a purchase of the product.
        Reduces quantity and returns total price.
        """
        if quantity > self.quantity:
            raise ValueError(f"Not enough quantity of {self.name} in stock.")
        self.quantity -= quantity
        return self.price * quantity


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()