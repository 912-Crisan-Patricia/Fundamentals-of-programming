import unittest
import entities
import repositories
import exceptions
import services
class Test(unittest.TestCase):
    book_id = 'ABC'
    book_title = 'The Fury'
    book_author = 'Nicholas Cage'
    bookrepo = repositories.BookRepository()
    clientrepo = repositories.ClientRepository()
    rentalrepo = repositories.RentalRepository()
    service = services.Services(bookrepo, clientrepo, rentalrepo)
    service.bookrepo.add_book(book_id, book_title, book_author)
    obtained_book = service.bookrepo.container[0]
    client_id = 'BBB'
    client_name = 'Sahara Grayson'
    service.clientrepo.add_client(client_id, client_name)
    obtained_client = service.clientrepo.container[0]
    rental_id = 'SBC'
    service.rentalrepo.add_rental(rental_id, book_id, client_id)
    def test_add(self):
        self.assertEqual(Test.book_id,Test.obtained_book.book_id)
        self.assertEqual(Test.book_title,Test.obtained_book.title)
        self.assertEqual(Test.book_author,Test.obtained_book.author)
        self.assertEqual(Test.client_id,Test.obtained_client.client_id)
        self.assertEqual(Test.client_name,Test.obtained_client.name)
    def test_remove(self):
        Test.service.delete_book(Test.book_id)
        self.assertEqual(len(Test.service.rentalrepo) , 0)
        self.assertEqual(len(Test.service.bookrepo) , 0)
        Test.service.delete_client(Test.client_id)
        self.assertEqual(len(Test.service.clientrepo), 0)
    def test_update(self):
        Test.service.bookrepo.add_book(Test.book_id, Test.book_title, Test.book_author)
        Test.service.clientrepo.add_client(Test.client_id, Test.client_name)
        Test.service.rentalrepo.add_rental(Test.rental_id, Test.book_id, Test.client_id)
        Test.service.update_book(Test.book_id,'blabla','Golem','Meyrink')
        obtained_book = Test.service.bookrepo.container[0]
        obtained_rental = Test.service.rentalrepo.container[0]
        self.assertEqual(obtained_book.book_id, 'blabla')
        self.assertEqual(obtained_book.title, 'Golem')
        self.assertEqual(obtained_book.author, 'Meyrink')
        self.assertEqual(obtained_rental.book_id, 'blabla')
        Test.service.update_client(Test.client_id, 'CCC', 'Johnny Bravo')
        Test.obtained_client = Test.service.clientrepo.container[0]
        self.assertEqual(Test.obtained_client.client_id , 'CCC')
        self.assertEqual(Test.obtained_client.name , 'Johnny Bravo')
        self.assertEqual(obtained_rental.client_id , 'CCC')
if __name__ == '__main__':
    unittest.main()