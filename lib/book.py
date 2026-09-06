#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count #underscore so we can control changes via the setter below

    @property
    def page_count(self):
        #returns the current page count
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        # only allow whole numbers otherwise yell abt it
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # pretends to flip a pafe in the book and prints a message
        print("Flipping the page...wow, you read fast!")
        
    
         