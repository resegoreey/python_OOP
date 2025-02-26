class Book:
    def __init__(self, title, author, ISBN, available_copies):
        self. title = title
        self.author = author
        self.ISBN = ISBN
        self.available_copies = available_copies

    def borrow_book(self, title):
        self.tile = title
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"You borrowed a book {title}, by {self.author}, ISBN: {self.ISBN} ")
        else:
            print("{title} not found on the shelf")
        pass

    def return_book(self, title):
        self.title = title
        self.available_copies += 1
        print(f"You returned the book {title}, by {self.author}, ISBN: {self.ISBN}. ")
        pass

    def check_availability(self, title):
        self.title = title
        if self.available_copies > 0:
            print(f"{self.available_copies} copies of {title} is available")
        else:
            print(f"No copies of {title} is available")
        pass

library = Book("Nothing but the truth", "John Kani", "223-445-565-67", 45)
library.borrow_book("Nothing but the truth")
#library.return_book("Nothing but the truth")
library.check_availability("Nothing but the truth")