class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.display()

    def search_book(self):
        title = input("Enter book title: ")
        for book in self.books:
            if book.title == title:
                print("Book found")
                book.display()
                return
        print("Book not found.")
    
    def borrow_book(self):
        title = input("Enter book title: ")
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print("Not available.")

    def return_book(self):
        title = input("Enter book title: ")
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print("Book not found.")
