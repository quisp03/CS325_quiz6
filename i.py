from abc import ABC, abstractmethod

# i.py

class SearchBooks(ABC):
    @abstractmethod
    def search_books(self):
        pass

class ManageBooks(ABC):
    @abstractmethod
    def add_book(self):
        pass

    @abstractmethod
    def remove_book(self):
        pass

class BorrowAndReturnBooks(ABC):
    @abstractmethod
    def borrow_book(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

class GenerateReport(ABC):
    @abstractmethod
    def generate_reports(self):
        pass

class GuestUser(SearchBooks):
    def search_books(self):
        print("Searching books")

class Librarian(SearchBooks, ManageBooks, BorrowAndReturnBooks, GenerateReport):
    def add_book(self):
        print("Adding book")

    def remove_book(self):
        print("Removing book")

    def borrow_book(self):
        print("Borrowing book")
    
    def return_book(self):
        print("Returning book")

    def generate_reports(self):
        print("Generating reports")

    def search_books(self):
        print("Searching books")


    
def main():

        librarian = Librarian()
        guest = GuestUser()

        librarian.add_book()
        librarian.remove_book()
        librarian.search_books()
        librarian.borrow_book()
        librarian.return_book()
        librarian.generate_reports()
        guest.search_books()


if __name__ == "__main__":
    main()