import services as fnct
import repositories
import random
import entities
import exceptions
class UI(object):
    def __init__(self,bookrepo,clientrepo,rentalrepo):
        self.services = fnct.Services(bookrepo,clientrepo,rentalrepo)
    def __display_menu(self):
        print(
            """
                   MENU
                1.Add a book
                2.Add a client
                3.Remove a book
                4.Remove a client
                5.Update a book
                6.Update a client
                7.List the books
                8.List the clients
                9.Rent a book
                10.Return a book
                11.Search a book
                12.Search a client
                13.Show most rented books
                14.Show most active clients
                15.Show most rented authors
                16.Exit            
            """
        )
    def __read_command(self):
        try:
            command = int(input('>'))
            assert command in range(1,17)
            if command == 1:
                book_id = input("Enter the book's ID: ")
                title = input("Enter the book's title: ")
                author = input("Enter the book's author: ")
                self.services.bookrepo.add_book(book_id,title,author)
            elif command == 2:
                client_id = input("Enter the client's ID>")
                name = input("Enter the client's name>")
                self.services.clientrepo.add_client(client_id,name)
            elif command == 3:
                book_id = input("Enter the book's ID>")
                self.services.delete_book(book_id)
            elif command == 4:
                client_id = input("Enter the client's ID>")
                self.services.delete_client(client_id)
            elif command == 5:
                book_id = input("Enter the book's ID>")
                newId = input("Enter the book's new ID(Press enter if you don't want to modify this)>")
                newTitle = input("Enter the book's new title(Press enter if you don't want to modify this)>")
                newAuthor = input("Enter the book's new author(Press enter if you don't want to modify this)>")
                self.services.update_book(book_id,newId,newTitle,newAuthor)
            elif command == 6:
                client_id = input("Enter the client's ID>")
                newId = input("Enter the client's new ID(Press enter if you don't want to modify this)>")
                newName = input("Enter the client's new name(Press enter if you don't want to modify this)>")
                self.services.update_client(client_id,newId,newName)
            elif command == 7:
                print(self.services.bookrepo)
            elif command == 8:
                print(self.services.clientrepo)
            elif command == 9:
                rental_id = input("Enter the rental's ID>")
                book_id = input("Enter the book's ID>")
                client_id = input("Enter the client's ID>")
                self.services.add_rental(rental_id,book_id,client_id)
            elif command == 10:
                rental_id = input("Enter the rental's ID>")
                self.services.rentalrepo.return_book(rental_id)
            elif command == 11:
                keyword = input("Enter the word by which you want to search>")
                l = self.services.search_book(keyword)
                for book in l:
                    print(book)
            elif command == 12:
                keyword = input("Enter the word by which you want to search>")
                l = self.services.search_client(keyword)
                for client in l:
                    print(client)
            elif command == 13:
                l = self.services.most_rented_books()
                print("Here are the most rented books in descending order:>")
                for id in l:
                    print(f"Book with id {id} with {l[id]} rentals>")
            elif command == 14:
                l = self.services.most_active_clients()
                print("Here are the most active clients in descending order:>")
                for id in l:
                    print(f"Client with id {id} with {l[id]} rentals>")
            elif command == 15:
                l = self.services.most_active_authors()
                print("Here are the most rented authors in descending order:>")
                for key in l:
                    print(f"Author {key} with {l[key]} rentals>")
            elif command == 16:
                exit(0)
        except KeyboardInterrupt:
            print("Goodbye!")
        except Exception as ex:
            print(ex)
            self.__display_menu()

    def loop_menu(self):
        self.__display_menu()
        while True:
            print(rentalrepo)
            self.__read_command()


if __name__ == '__main__':
    titles = ['The power of Habit' , 'Invitatie la vals' , 'The question book' , 'The power of now' ,'Monday' , 'The Pilgrim' , "Pride and prejudice" ]
    authors = ['Stephen King ' , 'Jordan Peterson' , 'Robert Green' , 'Jane Smith' ,'Samantha Jones' , 'Will James' , 'Michael Williams']
    charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    names = ['Jordan' , 'Marius' , 'John' , 'Steve' , 'Michael' , 'Andrew' , 'Jada' ,'William' , 'Chad' , 'Peter' , 'Christian']
    bookrepo = repositories.BookRepository()
    clientrepo = repositories.ClientRepository()
    rentalrepo = repositories.RentalRepository()
    while len(bookrepo) < 7:
        id = random.choice(charset) + random.choice(charset) + random.choice(charset)
        title = random.choice(titles)
        author = random.choice(authors)
        try:
            bookrepo.add_book(id,title,author)
            titles.remove(title)
            authors.remove(author)
        except:
            pass
    while len(clientrepo) < 7:
        id = random.choice(charset) + random.choice(charset) + random.choice(charset)
        name = random.choice(names) + ' ' + random.choice(names)
        try:
            clientrepo.add_client(id,name)
        except:
            pass
    client1 = random.choice(clientrepo.container)
    client2 = random.choice(clientrepo.container)
    id1 = client1.client_id
    id2 = client2.client_id
    while len(rentalrepo) < 7:
        client_id = random.choice([id1,id2])
        book_id = random.choice(bookrepo.container).book_id
        rental_id = random.choice(charset) + random.choice(charset) + random.choice(charset)
        #print(rental_id,book_id,client_id,sep='----')
        try:
            rentalrepo.add_rental(rental_id,book_id,client_id)
           # print(rentalrepo)
        except:
            pass
    UI = UI(bookrepo,clientrepo,rentalrepo)
    l = UI.services.most_active_authors()
    UI.loop_menu()
