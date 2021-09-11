class LibrarySys:

    def __init__(self, books):
        self.book_list = books
        self.lend_book_dict = {}

    def add_book(self, book_name):
        self.book_list.append(book_name)

    def lend_book(self, book_name, lender_name):
        if book_name in self.book_list:
            self.lend_book_dict[book_name] = lender_name
            self.book_list.remove(book_name)
            print(f"Book {book_name} has been successfully assigned to {self.lend_book_dict[book_name]}")
        elif book_name in self.lend_book_dict.keys():
            print(f"Sorry book is currently owned by : {self.lend_book_dict[book_name]}")
        else:
            print("Book NA in Lib")

    def return_book(self, book_name):

        if book_name in self.lend_book_dict.keys():
            self.book_list.append(book_name)
            print(f"Book is returned by {self.lend_book_dict[book_name]}")
            del self.lend_book_dict[book_name]
        else:
            print("Invalid Return")

    def display_books(self):
        print(self.book_list)


lib = LibrarySys(["Physics", "Chemistry", "Biology", "Computer", "IT Book", "Java", "JS"])

lib.display_books()
lib.add_book("HC Verma")
lib.display_books()

lib.return_book("any book")

lib.lend_book("Physics", "satya")
lib.display_books()

lib.return_book("Physics")

lib.display_books()
