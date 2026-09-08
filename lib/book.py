class Book:
    """Represents a book that can be read online, page by page."""

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """Return the current page count."""
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Simulate turning a page while reading the book."""
        print("Flipping the page...wow, you read fast!")