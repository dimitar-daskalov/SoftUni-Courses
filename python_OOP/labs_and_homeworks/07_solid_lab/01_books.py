# SRP (Single Responsibility Principle)

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class ReaderBookStatus:
    def __init__(self, book):
        self.book = book
        self.page = 0

    def turn_page(self, page: int):
        self.page = page


class Library:
    def __init__(self, books: list):
        self.books = books

    def find_book(self, title: str):
        try:
            book = [book for book in self.books if book.title == title][0]
            return book
        except IndexError:
            print(f"Book {title} is not in the library!")

    def add_book(self, book):
        self.books.append(book)




