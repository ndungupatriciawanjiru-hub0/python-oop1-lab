class Coffee:
    """Represents a coffee item sold by the bookstore."""

    VALID_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        # Use the setter below so size is validated on creation
        self.size = size
        # Store the price of the coffee
        self.price = price

    @property
    def size(self):
        """Return the current size."""
        return self._size

    @size.setter
    def size(self, size):
        # Only accept Small, Medium, or Large
        if size in self.VALID_SIZES:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """Add a tip for the coffee, increasing its price by 1."""
        print("This coffee is great, here\u2019s a tip!")
        self.price += 1