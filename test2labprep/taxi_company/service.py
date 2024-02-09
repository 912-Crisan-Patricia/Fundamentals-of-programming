from domain import Address
from repo import *

class Service:
    def __init__(self,repo) -> None:
        self.repo=repo

    def add_address(self, id, name, number, x, y):
        if not id.isdigit():
            raise ValueError("Id not a digit")
        if len(name) < 4:
            raise ValueError("Name too short")
        if not number.isdigit() or int(number) <0 or int(number)>100:
            raise ValueError("Number not a digit")
        '''
        if not x.isdigit() or int(x) <-100 or int(x)>100 :
            raise ValueError("Something wrong with value x")
        if not y.isdigit() or int(y) <-100 or int(y)>100:
            raise ValueError("Y not a digit")        
        '''
        try:
            int(x)
        except:
            raise ValueError("X must be an integer")
        if int(x)>100 or int(x)<-100:
            raise ValueError("X must be an integer between -100 and 100")
        try:
            int(y)
        except:
            raise ValueError("Y must be an integer")
        if int(y)>100 or int(y)<-100:
            raise ValueError("Y must be an integer between -100 and 100")


        address=Address(int(id) ,name , int(number),int(x), int(y))
        self.repo.add_address(address)

    def get_addresses(self):
        return self.repo.get_addresses_as_string()

    def get_distance(self,x,y,d):
        try:
            int(x)
        except:
            raise ValueError("X must be an integer")
        if int(x)>100 or int(x)<-100:
            raise ValueError("X must be an integer between -100 and 100")
        try:
            int(y)
        except:
            raise ValueError("Y must be an integer")
        if int(y)>100 or int(y)<-100:
            raise ValueError("Y must be an integer between -100 and 100")

        addresses=self.repo.get_addresses()
        new_adresses=[]
        for address in addresses:
            distance= ((address.get_x() - int(x))**2 + (address.get_y()- int(y))**2)**(1/2)
            if distance <= int(d):
                new_adresses.append((address, distance))
        return new_adresses


