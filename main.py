class Library():
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def library_name(self):
        print(f"Welcome to {self.name} library!")

    def list_books(self):
        print('This library has the following books:')

        for book in self.books:
            print(f'{book.title} by {book.author}')

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book('Fasz1', 'Fasz1')
book2 = Book('Fasz2', 'Fasz2')
book3 = Book('Fasz3', 'Fasz3')

library = Library('Könyvtár')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()


        

