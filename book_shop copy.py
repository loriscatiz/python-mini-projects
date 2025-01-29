import sys
sys.path.append('../modules')
from modules import utils
class Book:
    def __init__(self, title: str) -> None:
        self.title = title

class Bookstore:
    def __init__(self, books_in_stock: dict[str, int], books_to_be_ordered: dict[str, int], books_sold: dict[str, int],) -> None:
        self.books_in_stock: dict[str, int] = {}
        self.books_to_be_ordered: dict[str, int] = {}
        self.books_sold: dict[str, int] = {}

    def add_book(self, book: Book, quantity: int):
        if book.title in self.books_in_stock:
            self.books_in_stock[book.title] += quantity
        else:
            self.books_in_stock[book.title] = quantity

    def sell_book(self, book: Book):
        try: 
            self.books_in_stock[book.title] -= 1
        except KeyError:
            if book.title in self.books_to_be_ordered:
                self.books_to_be_ordered[book.title] += 1
            else:
                self.books_to_be_ordered[book.title] = 1
        else:
            if book.title in self.books_sold:
                self.books_sold[book.title] += 1
            else:
                self.books_sold[book.title] = 1
            print(f'{book.title} Sold')
            print("$$$")
            if not self.books_in_stock[book.title]:
                self.books_in_stock.pop(book.title)

    def show_inventory(self):
        print("Current situation: ")
        print(f"Books in stock: {self.books_in_stock}")
        print(f"Books to be ordered: {self.books_to_be_ordered}")
        print(f"Books sold: {self.books_sold}")

def main():
    my_store = Bookstore({}, {}, {})
    my_store.show_inventory() 

    while True:
        print("What do you wanna do?")
        print("'A' to add a book")
        print("'S' to sell a book (if not in stock, will be added 1 book to be ordered)")
        print("'Q' to quit")
        action = utils.get_string_accepted_values(['A', 'S', 'Q'])
        match action:
            case "A":
                my_store.add_book(Book(input("What's the title")), utils.get_int_greater_or_equal_than(1))
            case "S":
                my_store.sell_book(Book(input("What's the title")))
            case "Q":
                break            
            case _:
                pass
    my_store.show_inventory()
        

if __name__ == '__main__':
    main()