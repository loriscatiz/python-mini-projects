books_in_stock: dict[str, int] = {
    "1984": 5,
    "To Kill a Mockingbird": 8,
    "The Great Gatsby": 6,
    "Moby Dick": 4,
    "Pride and Prejudice": 10,
    "War and Peace": 3,
    "The Catcher in the Rye": 7,
    "Brave New World": 5,
    "The Hobbit": 9,
    "Fahrenheit 451": 6,
    "Crime and Punishment": 4,
    "The Lord of the Rings": 3,
    "Dracula": 7,
    "The Odyssey": 5,
    "The Divine Comedy": 3,
    "Les Misérables": 4,
    "Jane Eyre": 8,
    "Wuthering Heights": 6,
    "The Picture of Dorian Gray": 5,
    "Don Quixote": 2
}

books_to_be_ordered: dict[str, int] = {}
books_sold: dict[str, int] = {}


def add_to_dictionary(book: str , books_dictionary: dict[str, int]):
        if book not in books_dictionary:
            books_dictionary.update({book: 1})
        else:
            books_dictionary.update({book: books_dictionary[book] + 1})


def get_book(book: str) -> tuple[dict[str, int], dict[str, int], dict[str, int]]:
    try:
        books_in_stock[book] -=1
    except KeyError:
        print('Book not in stock')
        add_to_dictionary(book, books_to_be_ordered)
    else:
        print("Stonks $$$") 
        add_to_dictionary(book, books_sold)
        if books_in_stock[book] == 0:
            books_in_stock.pop(book)
    finally:
        print('This finally does nothing')

    print(f"Sold books: {books_sold}")
    print(f"Books to be ordered: {books_to_be_ordered}")
    print(f"Books in stock: {books_in_stock}")

    return(books_sold, books_to_be_ordered, books_in_stock)


if __name__ == '__main__':
    get_book('Biancaneve e i 7 cazzi')
    get_book('Don Quixote')
    get_book('Don Quixote')
    get_book('Don Quixote')
