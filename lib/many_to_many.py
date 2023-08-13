from datetime import datetime

class Author:
    all_author = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("name must be string")
        self.name = name
        Author.all_author.append(self)
    def contracts(self):
        return [contract for contract in Contract.all_contract if contract.author == self]
    def books(self):
        return [contract.book for contract in Contract.all_contract if contract.author == self]
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all_book = []
    def __init__(self, title):
        if not isinstance(title, str):
            raise ValueError("title must be a string")
        self.title = title
        Book.all_book.append(self)
    def contracts(self):
        return [contract for contract in Contract.all_contract if contract.book == self]
    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all_contract = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("author must be instance of class Author")
        self.author = author
        if not isinstance(book, Book):
            raise ValueError("book must be instance of Book Class")
        self.book = book
        if not isinstance(date, str):
            raise ValueError("date must be string")
        self.date = date
        if not isinstance(royalties, int):
            raise ValueError("royalties must be integer")
        self.royalties = royalties
        Contract.all_contract.append(self)
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all_contract, key=lambda contract: datetime.strptime(contract.date, "%d/%m/%Y"))
