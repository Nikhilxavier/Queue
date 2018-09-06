"""
Implementation of a Deque.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


class Deque:
    """Deque class with inbuilt functions."""

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
