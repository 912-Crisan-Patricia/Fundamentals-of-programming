class Address:
    def __init__(self,id,name,number,x,y):
        self.id=id
        self.name=name
        self.number= number
        self.x= x
        self.y= y


    #getters

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self) -> str:
        return str(self)

    def __str__(self)-> str:
        return str(self.id)+","+str(self.name)+","+str(self.number)+","+str(self.x)+ ","+str(self.y)


