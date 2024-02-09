from domain import Address

class Repo:
    def __init__(self,path) -> None:
        self.path=path
        self.addresses=[]
        self.load_file()



    def load_file(self):
        with open(self.path,"r") as f:
            for line in f:
                tokens= line.split(",")
                self.addresses.append(Address(int(tokens[0]),tokens[1],int(tokens[2]),int(tokens[3]),int(tokens[4])))

    def save_file(self):
        with open(self.path,"w") as f:
            for address in self.addresses:
                string_address= str(address.get_id())+","+str(address.get_name())+","+str(address.get_number())+","+str(address.get_x())+","+str(address.get_y())+"\n"
                f.write(string_address)

    def add_address(self,newaddress):
        for address in self.addresses:
            if newaddress.get_id() == address.get_id():
                raise ValueError("Adress already in system")
        self.addresses.append(newaddress)
        self.save_file()

    def get_addresses(self):
        return self.addresses

    def get_addresses_as_string(self):
        string=""
        for address in self.addresses:
            string+=str(address)
            string+='\n'
        return string





