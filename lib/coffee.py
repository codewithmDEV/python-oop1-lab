#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self._size = size #goes through the setter below to validate
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        # only these 3 sizes are allowed, anything else gets rejected
        if size in ("Small", "Medium", "Large"):
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # tipping makes the coffee cost a bit more, obviously
        print("This coffee is great, here’s a tip!")
        self.price += 1