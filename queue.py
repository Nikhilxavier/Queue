"""
Implementation of a Queue.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


class Queue:
    """Queue class with inbuilt functions."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
