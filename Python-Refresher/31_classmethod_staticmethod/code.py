class Book:
    TYPES = ("Hardcover", "Paperback", "Kindle Edition")
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type} weighs {self.weight} grams>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)

    @classmethod
    def kindle(cls, name, page_weight):
        return cls(name, cls.TYPES[2], page_weight)

book1 = Book.hardcover("Harry Potter", 1500)
book2 = Book.paperback("Phantom Comics", 10)
book3 = Book.kindle("Python is easy","NA")
print (book1)
print (book2)
print (book3)


