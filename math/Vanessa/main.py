#!/usr/bin/env python3
import sys


class LibraryItem:
    count = 0

    def __intit__(self, title):
        self.borrowed = False
        title = self.title

    def borrow(self):
        if self.borrowed == True:
            print("Book already borrowed")
        else:
            self.borrowed = True

    def return_item(self):
        self.borrowed = False

    def get_info(self):
        print(f"Item ID : {self.id} , title : {self.title}")


class Book(LibraryItem):
    def __init__(self, author_name, pages):
        super().__init__(self)
        self.author_name = author_name
        self.number_pages = pages

    def get_info(self):
        str = f": title = {self.title}, "


if __name__ == "__main__":
    answer = 0
    while answer != "1" or answer != "3" or answer != "6":
        print("1. Add a book")
        print("3. View all books")
        print("6. Export library to JSON file")
        input("Enter your choice: ")
        print()

        if answer == "1":
            book_title = input("title")
            author_name = input("author")
            number_pages = input("number of pages")
