class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        print("====================")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        if self.available:
            print("Available: Yes")
            print("====================")
        else:
            print("Available: No")
            print("====================")

    def borrow(self):
        if self.available:
            self.available = False
            print("Book brorowde successfully.")
        else:
            print("Not available.")


    def return_book(self):
        self.available = True
        print("Book returned.")