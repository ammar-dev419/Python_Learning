from Library_class import *
from Book_class import *
library = Library()

while True:
    print("1. Add book")
    print("2. Show book")
    print("3. Search")
    print("4. Borrow")
    print("5. Return")
    print("6. Exit")
    command_list = str(input("Choisissez votre commande: "))
    if command_list == "1":
        title = input("Title: ")
        author = input("Author: ")
        book = Book(title, author)
        library.add_book(book)
    
    elif command_list == "2":
        library.show_books()
    
    elif command_list == "3":
        library.search_book()
    
    elif command_list == "4":
        library.borrow_book()
    
    elif command_list == "5":
        library.return_book()

    elif command_list == "6":
        break

    else:
        print("Commande invalide.")