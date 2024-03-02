from abc import ABC, abstractmethod

# i.py
# This program was made to apply ISP or the 'Interface Segregation Principle'
# This principle states that clients should not have dependcies on unused interfaces.
# Interfaces should be broken down to handle smaller and specific interfaces.
# The benefit here is so that the client can only use methods relevant to their functions.
# Interfaces were created to define specific functionalities.
# As such, they are limited to the classes that need the particular functionalities.

class SearchBooks(ABC):
    # Abstract base class defining search_books method
    @abstractmethod
    def search_books(self):
        pass

class ManageBooks(ABC):
    # Abstract base class defining add_book and remove_book methods
    @abstractmethod
    def add_book(self):
        pass

    @abstractmethod
    def remove_book(self):
        pass

class BorrowAndReturnBooks(ABC):
    # Abstract base class defining borrow_book and return_book methods
    @abstractmethod
    def borrow_book(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

class GenerateReport(ABC):
    # Abstract base class defining generate_reports method
    @abstractmethod
    def generate_reports(self):
        pass

class GuestUser(SearchBooks):
    # Implements SearchBooks interface therefore only utilizing search_books method
    def search_books(self):
        print("Searching books")

class Librarian(SearchBooks, ManageBooks, BorrowAndReturnBooks, GenerateReport):
    # All interfaces are implemented therefore class Librarian utilizies all methods in regards to these interfaces
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
        # Assigning variables to data
        librarian = Librarian()
        guest = GuestUser()
        # Test functinality
        librarian.add_book()
        librarian.remove_book()
        librarian.search_books()
        librarian.borrow_book()
        librarian.return_book()
        librarian.generate_reports()
        guest.search_books()


if __name__ == "__main__":
    main()