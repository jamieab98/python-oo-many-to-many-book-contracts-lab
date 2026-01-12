from datetime import datetime

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def __repr__(self):
        return (f"Author: {self.name}")
    
    def books(self):
        books = [contract.book for contract in Contract.all if contract.author == self]
        print(books)
    
    def sign_contracts(self, book, royalties):
        Contract(self, book, royalties)
    
    def total_royalties(self):
        return ('''total amount of royalties from contracts''')

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def __repr__(self):
        return (f"Book {self.title}")
    
    def contracts(self):
        return ('''List of related contracts''')
    
    def authors(self):
        return ('''List of related authors''')
    

class Contract:
    all = []

    def __init__(self, author, book, royalties):
        self.author = author
        self.book = book
        self.date = datetime.now()
        self.royalties = royalties
        Contract.all.append(self)


author1 = Author("Jamie")
author2 = Author("Micahel")

book1 = Book("The Life of Pi")
book2 = Book("The Subtle Art of Not Giving a F*ck")
book3 = Book("If you Give a Mouse a Cookie")

author1.sign_contracts(book1, 50)
author1.sign_contracts(book2, 10)
author2.sign_contracts(book2, 40)
author2.sign_contracts(book3, 20)

author1.books()
