# Import the math module
import math


# =========================
# Create the Pagination class
# =========================

class Pagination():

    # Constructor
    def __init__(self, items=None, page_size=10):

        # If items is None, create an empty list
        if items is None:
            items = []

        # Initialize attributes
        self.items = items
        self.page_size = page_size
        self.current_idx = 0

        # Calculate the total number of pages
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    # =========================
    # Method to get visible items
    # =========================
    def get_visible_items(self):

        # Calculate start and end indexes
        start = self.current_idx * self.page_size
        end = start + self.page_size

        # Return the visible items
        return self.items[start:end]

    # =========================
    # Go to a specific page
    # =========================
    def go_to_page(self, page_num):

        # Check if page number is valid
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number out of range")

        # Convert page number to index
        self.current_idx = page_num - 1

        return self

    # =========================
    # Go to the first page
    # =========================
    def first_page(self):

        self.current_idx = 0
        return self

    # =========================
    # Go to the last page
    # =========================
    def last_page(self):

        self.current_idx = self.total_pages - 1
        return self

    # =========================
    # Go to the next page
    # =========================
    def next_page(self):

        # Check if not already on last page
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1

        return self

    # =========================
    # Go to the previous page
    # =========================
    def previous_page(self):

        # Check if not already on first page
        if self.current_idx > 0:
            self.current_idx -= 1

        return self

    # =========================
    # Custom string method
    # =========================
    def __str__(self):

        # Return items line by line
        return "\n".join(self.get_visible_items())


# =========================
# Test the Pagination class
# =========================

# Create a list of alphabet letters
alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# Create a Pagination object
p = Pagination(alphabetList, 4)

# Display visible items
print(p.get_visible_items())

# Go to next page
p.next_page()
print(p.get_visible_items())

# Go to last page
p.last_page()
print(p.get_visible_items())

# Test invalid page number
try:
    p.go_to_page(10)
except ValueError as error:
    print(error)

# Test another invalid page number
try:
    p.go_to_page(0)
except ValueError as error:
    print(error)

# Test method chaining
print(
    p.first_page()
     .next_page()
     .next_page()
     .next_page()
     .get_visible_items()
)

# Test __str__ method
print(str(p))