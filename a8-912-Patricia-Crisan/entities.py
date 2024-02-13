class Book(object):
    def __init__(self,id,title,author):
        self.__book_id = id
        self.__title = title
        self.__author = author
    @property
    def book_id(self):
        return self.__book_id
    @book_id.setter
    def book_id(self,newId):
        self.__book_id = newId
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self,newTitle):
        self.__title = newTitle
    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self,newAuthor):
        self.__author = newAuthor
    def __eq__(self, other):
        return self.book_id == other.book_id
    def __str__(self):
        return f"Book with id {self.__book_id} , title {self.__title} , author {self.__author}"

class Client(object):
    def __init__(self,id,name):
        self.__client_id = id
        self.__name = name
    @property
    def client_id(self):
        return self.__client_id
    @client_id.setter
    def client_id(self,newId):
        self.__client_id = newId
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,newName):
        self.__name = newName
    def __eq__(self, other):
        return self.client_id == other.client_id
    def __str__(self):
        return f"Client with id {self.__client_id} named {self.name}"

class Rental(object):
    def __init__(self, id, book_id, client_id, rented_date = 0, returned_date = 0):
        self.__rental_id = id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date
    @property
    def rental_id(self):
        return self.__rental_id
    @property
    def book_id(self):
        return self.__book_id
    @property
    def client_id(self):
        return self.__client_id
    @property
    def rented_date(self):
        return self.__rented_date
    @property
    def returned_date(self):
        return self.__returned_date
    def set_returned_date(self,date):
        self.__returned_date = date
    def set_book_id(self,id):
        self.__book_id = id
    def set_client_id(self,id):
        self.__client_id = id
    def __eq__(self, other):
        return self.rental_id == other.rental_id or (self.book_id == other.book_id and (not self.__returned_date and not other.__returned_date) or (self.__returned_date and other.__returned_date))
    def __str__(self):
        returned = f"and returned on {self.__returned_date}"
        if self.__returned_date == 0:
            returned = ", not yet returned"
        return f"Rental with id {self.__rental_id} , book {self.__book_id} , client {self.client_id} " \
               f"rented on {self.__rented_date} " + returned
