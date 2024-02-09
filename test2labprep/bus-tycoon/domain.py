class Routes:
    def __init__(self,code ,length):
        self.code= code
        self.length=length
    #getters
    def getCode(self):
        return self.code

    def getLength(self):
        return self.length

    #setters
    def setCode(self,code):
        self.code=code

    def setLength(self,length):
        self.length=length

    def __str__(self):
        return str(self.code) + "," + str(self.length)

class Bus:
    def __init__(self,id, code,model,time):
        self.id=id
        self.code=code
        self.model=model
        self.time=time

    #getters
    def getId(self):
        return self.id

    def getCode(self):
        return self.code

    def getModel(self):
        return self.model

    def getTime(self):
        return self.time

    #setters
    def setId(self,id):
        self.id=id

    def setCode(self,code):
        self.code=code

    def setModel(self,model):
        self.model=model

    def setTime(self,time):
        self.time=time

    def __str__(self):
        return str(self.id) + "," + str(self.code) + "," + str(self.model) + "," + str(self.time)