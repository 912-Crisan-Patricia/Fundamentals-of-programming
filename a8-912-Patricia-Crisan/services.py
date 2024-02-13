import entities
import exceptions
import repositories
from datetime import date
class Services(object):
    def __init__(self,bookrepo,clientrepo,rentalrepo):
        self.__bookrepo = bookrepo
        self.__clientrepo = clientrepo
        self.__rentalrepo = rentalrepo
    @property
    def bookrepo(self):
        return self.__bookrepo
    @property
    def clientrepo(self):
        return self.__clientrepo
    @property
    def rentalrepo(self):
        return self.__rentalrepo
    def delete_book(self,book_id):
        """
        Searches for the book with given id and deletes it from the Book repository and Rental Repository
        :param book_id:  string
        :return:
        """
        dump_book = entities.Book(book_id,'aa','aa')
        if dump_book in self.__bookrepo:
            self.__bookrepo.container.remove(dump_book)
            index = len(self.__rentalrepo.container) - 1
            while index >= 0:
                if self.__rentalrepo.container[index].book_id == book_id:
                    del self.__rentalrepo.container[index]
                index -= 1
        else:
            raise exceptions.NotFound("Entered book not found!")
        del dump_book
    def delete_client(self,client_id):
        """
        Searches for a client with the given id and deletes it from client repository and rental repository
        :param client_id:string
        :return:
        """
        dump_client = entities.Client(client_id, 'aa')
        if dump_client in self.__clientrepo:
            self.__clientrepo.container.remove(dump_client)
            index = len(self.__rentalrepo.container) - 1
            while index >= 0:
                if self.__rentalrepo.container[index].client_id == client_id:
                    del self.__rentalrepo.container[index]
                index -= 1
        else:
            raise exceptions.NotFound("Entered client not found!")
    def update_book(self,book_id,newId,newTitle,newAuthor):
        """
        Searches for a book with the given id and updates it's attributes
        :param book_id: string
        :param newId: string
        :param newTitle: string
        :param newAuthor: string
        :return:
        """
        dump_book = entities.Book(book_id, 'aa', 'aa')
        check = False
        if dump_book in self.__bookrepo:
            index = self.__bookrepo.container.index(dump_book)
            if newId != '':
                self.__bookrepo.container[index].book_id = newId
                check = True
            if newTitle != '':
                self.__bookrepo.container[index].title = newTitle
            if newAuthor != '':
                self.__bookrepo.container[index].author = newAuthor
            if check:
                for index,rental in enumerate(self.__rentalrepo.container):
                    if rental.book_id == book_id:
                        self.__rentalrepo.container[index].set_book_id(newId)
        else:
            raise exceptions.NotFound("Entered book not found!")
    def update_client(self,client_id,newId,newName):
        """
        Searches for a client with given id and updates it's attributes
        :param client_id:
        :param newId:
        :param newName:
        :return:
        """
        dump_client = entities.Client(client_id, 'aa')
        check = False
        if dump_client in self.__clientrepo:
            index = self.__clientrepo.container.index(dump_client)
            if newId != '':
                self.__clientrepo.container[index].client_id = newId
                check = True
            if newName != '':
                self.__clientrepo.container[index].name = newName
            if check:
                for index,rental in enumerate(self.__rentalrepo.container):
                    if rental.client_id == client_id:
                        self.__rentalrepo.container[index].set_client_id(newId)
        else:
            raise exceptions.NotFound("Entered client not found!")
    def add_rental(self,rental_id,book_id,client_id):
        """
        Checks if a rental can be added to the repo(if given book and client exists)
        :param rental_id: string
        :param book_id:string
        :param client_id:string
        :return:
        """
        dump_book = entities.Book(book_id, '', '')
        dump_client = entities.Client(client_id, '')
        if dump_book in self.bookrepo and dump_client in self.clientrepo:
            self.rentalrepo.add_rental(rental_id, book_id, client_id)
        else:
            raise exceptions.NotFound("Book or client not existing!")
    def search_book(self,keyword):
        """
        Searches and returns all the books that have the keyword in any attribute
        :param keyword: string
        :return:
        """
        result = []
        keyword = keyword.lower()
        for book in self.bookrepo.container:
            if keyword in book.book_id.lower() or keyword in book.title.lower() or keyword in book.author.lower():
                result.append(book)
        return result
    def search_client(self,keyword):
        """
        Searches and returns all the clients that have the keyword in any attribute
        :param keyword: string
        :return:
        """
        result = []
        keyword = keyword.lower()
        for client in self.clientrepo.container:
            if keyword in client.client_id.lower() or keyword in client.name.lower():
                result.append(client)
        return result
    def most_rented_books(self):
        """
        Determines the most rented books
        :return: dictionary
        """
        list = self.rentalrepo.container
        auxiliary = [book.book_id for book in self.rentalrepo.container]
        list.sort(key = lambda rental : auxiliary.count(rental.book_id) , reverse = True)
        result = {}
        for rental in list:
            if rental.book_id not in result:
                result[rental.book_id] = auxiliary.count(rental.book_id)
        return result
    def most_active_clients(self):
        """
        Determines the most active clients
        :return: dictionary
        """
        list = self.rentalrepo.container
        auxiliary = [rental.client_id for rental in list]
        list.sort(key = lambda rental : auxiliary.count(rental.client_id) * (rental.returned_date - rental.rented_date) if rental.returned_date != 0 else auxiliary.count(rental.client_id) * (date.today() - rental.rented_date), reverse = True)
        result = {}
        for rental in list:
            if rental.client_id not in result:
                result[rental.client_id] = auxiliary.count(rental.client_id) * (rental.returned_date - rental.rented_date) if rental.returned_date != 0 else auxiliary.count(rental.client_id) * (date.today() - rental.rented_date)
        return result
    def most_active_authors(self):
        """
        Determines the most active authors
        :return: dictionary
        """
        l = self.bookrepo.container
        rentals = self.rentalrepo.container
        dictionary = dict()
        for book in l:
            if book.author not in dictionary:
                dictionary[book.author] = 0
        iduri = [book.book_id for book in l]
        for rental in rentals:
            book_id = rental.book_id
            index = iduri.index(book_id)
            author = l[index].author
            dictionary[author] += 1
        result = dict(sorted(dictionary.items(), key=lambda item: item[1] , reverse = True))
        return result
def test():
    bookrepo = repositories.BookRepository()
    clientrepo = repositories.ClientRepository()
    rentalrepo = repositories.RentalRepository()
    bookrepo.add_book('ABC', 'aa', 'bb')
    s = Services(bookrepo,clientrepo,rentalrepo)
    print(bookrepo.container)
    s.delete_book('ABC')
    print(bookrepo.container)
    bookrepo.add_book('ABC', 'aa', 'bb')
    clientrepo.add_client('ASDA','barnea')
    rentalrepo.add_rental('BBB','ABC','ASDA')
    s.update_book('ABC','SBX','asd','bcv')
    print(bookrepo.container[0])
#test()
