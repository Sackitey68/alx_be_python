class Book:
    def __init__(self, title, author, year):
        """Constructor: Initialize the book's attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the book instance is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Human-readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Unambiguous representation of the book that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

