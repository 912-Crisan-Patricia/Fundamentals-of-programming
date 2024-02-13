import entities
import exceptions
from datetime import date
class BookRepository(object):
    def __init__(self):
        self._container = []
    @property
    def container(self):
        return self._container
    def add_book(self,id,title,author):
        """
        Instantatiates a book with the given attributes and adds it to the repository
        :param id: string denoting book's id
        :param title:string denoting book's title
        :param author:string denoting book's author
        :return:
        """
        book = entities.Book(id,title,author)
        if book in self.container:
            raise exceptions.RepositoryError("Book already existing!")
        self._container.append(book)
    def __contains__(self, item):
        return item in self.container
    def __str__(self):
        TBP = ''
        for object in self.container:
            TBP += str(object)
            TBP += '\n'
        if TBP == '':
            return 'Empty'
        return TBP
    def __len__(self):
        return len(self.container)

class ClientRepository(BookRepository):
    def add_client(self, id, name):
        """
        Instantiates a client with the given attributes and adds it to the repository
        :param id: client's id as a string
        :param name:client's name as a string
        :return:
        """
        client = entities.Client(id,name)
        if client in self.container:
            raise exceptions.RepositoryError("Client already existing!")
        self._container.append(client)

class RentalRepository(BookRepository):
    def add_rental(self,rental_id,book_id,client_id):
        """
        Instantiates a rental with the given attributes and adds it to the repository
        :param rental_id: string
        :param book_id: string
        :param client_id: string
        :return:
        """
        today = date(2022,12,18)
        rental = entities.Rental(rental_id,book_id,client_id,today)
        if rental in self.container:
            raise exceptions.RepositoryError("Rental already existing or book already rented!")
        self.container.append(rental)
    def return_book(self,rental_id):
        """
        Searches for the rental with the given id and if it exists,changes it as returned
        :param rental_id: string
        :return:
        """
        dump_rental = entities.Rental(rental_id,'','')
        if dump_rental in self.container:
            index = self.container.index(dump_rental)
            self.container[index].set_returned_date(date.today())
        else:
            raise exceptions.NotFound("Rental not found!")

def test():
    bookrepo = BookRepository()
    bookrepo.add_book('ABCD',"aaa",'bbb')
    print(bookrepo)
    #bookrepo.add_book('ABCD', "aaa", 'bbb')
    clientrepo = ClientRepository()
    clientrepo.add_client('ABCD','Patricia')
    print(clientrepo)
#test()