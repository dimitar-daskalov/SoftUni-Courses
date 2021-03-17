# DIP (Dependency Inversion Principle)

class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book, formatter: Formatter):
        formatted_book = formatter.format(book)
        return formatted_book


received_book = Book("Some content")
received_formatter = Formatter()

received_printer = Printer()
print(received_printer.get_book(received_book, received_formatter))