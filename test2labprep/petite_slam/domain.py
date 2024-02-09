class Player:
    def __init__(self,id,name,power):
        self.id = id
        self.name=name
        self.power= power

    #getters

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_power(self):
        return self.power

    def __str__(self):
        return str(self.id)+","+str(self.name)+","+str(self.power)