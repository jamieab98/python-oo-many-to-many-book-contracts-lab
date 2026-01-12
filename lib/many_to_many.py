from datetime import datetime

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def __repr__(self):
        return (f"Author {self.name}")
    
    def books(self):
        books = [contract.book for contract in Contract.all if contract.author == self]
        return books
    
    def contracts(self):
        contracts = [contract for contract in Contract.all if contract.author == self]
        return contracts
    
    def sign_contract(self, book, date, royalties):
        return (Contract(self, book, date, royalties))
    
    def total_royalties(self):
        royalty_amount = 0
        contracts = [contract for contract in Contract.all if contract.author == self]
        for contract in contracts:
            royalty_amount += contract.royalties
        return royalty_amount

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def __repr__(self):
        return (f"Book {self.title}")
    
    def contracts(self):
        contracts = [contract for contract in Contract.all if contract.book == self]
        return contracts
    
    def authors(self):
        authors = [contract.author for contract in Contract.all if contract.book == self]
        return authors
    

class Contract:
    all = []

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("The author must be an instance of Author")
        else:
            self._author = value
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("The book must be an instance of Book")
        else:
            self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("The date must be a string")
        else:
            self._date = value
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise TypeError("The royatly amount must be an integer")
        else:
            self._royalties = value

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def contracts_by_date(date):
        contracts = [contract for contract in Contract.all if contract.date == date]
        return (contracts)

author1 = Author("Jamie")
author2 = Author("Micahel")

book1 = Book("The Life of Pi")
book2 = Book("The Subtle Art of Not Giving a F*ck")
book3 = Book("If you Give a Mouse a Cookie")

author1.sign_contract(book1, "1/1/2001", 50)
author1.sign_contract(book2, "1/2/2001", 10)
author2.sign_contract(book2, "1/3/2001", 40)
author2.sign_contract(book3, "1/4/2001", 20)

author1.total_royalties()