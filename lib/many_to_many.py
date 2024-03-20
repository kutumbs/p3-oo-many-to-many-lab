class Author:

    all = []
    
    def __init__(self, name):
        self.name = name 
        #self.all.append(self)

    def contracts(self):
        all_contracts = Contract.all
        return [contract for contract in all_contracts if contract.author == self]
    
    def books(self):
        author_contracts = self.contracts()
        return [contract.book for contract in author_contracts ]
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        total_royalties = self.contracts()
        royalties = [contract.royalties for contract in total_royalties]
        return sum(royalties)




class Book:

    all = []

    def __init__(self, title):
        self.title = title
        #self.all.append(self)

    def contracts(self):
        all_contracts = Contract.all
        return [contract for contract in all_contracts if contract.book == self]
    
    def authors(self):
        book_authors = self.contracts()
        return [contract.author for contract in book_authors]
        


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and isinstance(book, Book):
            self.author = author
            self.book = book
        else:
            raise TypeError("Invalis types for author and/or book")
        
        if isinstance(date, str):
            self.date = date
        else:
            raise TypeError("date must be a string")
        
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise TypeError("royalties must be a number")
        
        Contract.all.append(self)


    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]