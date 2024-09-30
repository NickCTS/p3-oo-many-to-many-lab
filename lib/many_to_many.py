class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []  # Initialize an empty list to hold contracts
        self._books = []      # Initialize an empty list to hold books

    def add_contract(self, contract):
        """Add a contract to the author"""
        self._contracts.append(contract)
        if contract.book not in self._books:
            self._books.append(contract.book)

    def contracts(self):
        """Return the list of contracts"""
        return self._contracts

    def books(self):
        """Return the list of books"""
        return self._books

    def sign_contract(self, book, date, royalties):
        """Create a contract for the author and a book"""
        contract = Contract(self, book, date, royalties)
        self.add_contract(contract)
        return contract

    def total_royalties(self):
        """Get the sum of all royalties from contracts"""
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []  # Initialize an empty list to hold contracts

    def add_contract(self, contract):
        """Add a contract to the book"""
        self._contracts.append(contract)

    def contracts(self):
        """Return the list of contracts"""
        return self._contracts

    def authors(self):
        """Return a list of authors associated with this book"""
        return [contract.author for contract in self._contracts]


class Contract:
    all = []  # Class variable to hold all contracts

    def __init__(self, author, book, date, royalties):
        # Validate the input types
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)  # Add this contract to the class variable

        # Associate the contract with the author and book
        author.add_contract(self)
        book.add_contract(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Sort contracts by date and filter by given date"""
        return sorted([contract for contract in cls.all if contract.date == date], key=lambda x: x.date)
