from domain import Bus, Routes

class Repo:
    def __init__(self,pathbus,pathroutes):
        self.buses=[]
        self.routes=[]
        self.pathbus =pathbus
        self.pathroutes =pathroutes
        self.loadfile()

    def addbus(self,bus):
        for b in self.buses:
            if b.getId()==bus.getId():
                raise Exception("Bus already exists")
        self.buses.append(bus)

    def addroute(self,route):
        for r in self.routes:
            if r.getCode()==route.getCode():
                raise Exception("Route already exists")
        self.routes.append(route)
    def loadfile(self):
        f=open(self.pathroutes,"r")
        line=f.readline().strip()
        while line!="":
            tok=line.split(",")
            route=Routes(int(tok[0]),int(tok[1]))
            self.addroute(route)
            line=f.readline().strip()
        f.close()

        f = open(self.pathbus, "r")
        line = f.readline().strip()
        while line != "":
            tok = line.split(",")
            bus = Bus(int(tok[0]), int(tok[1]), tok[2], int(tok[3]))
            self.addbus(bus)
            line = f.readline().strip()
        f.close()


    def getbuses(self):
        return self.buses

    def getroutes(self):
        return self.routes

    def savefile(self):
        f=open(self.pathroutes,"w")
        for route in self.routes:
            f.write(str(route.getCode())+","+str(route.getLength())+"\n")
        f.close()

        f=open(self.pathbus,"w")
        for bus in self.buses:
            f.write(str(bus.getId())+","+str(bus.getCode())+","+str(bus.getModel())+","+str(bus.getTime())+"\n")
        f.close()


    def display_buses_string(self):
        string=""
        for bus in self.buses:
            string+=str(bus)
            string+='\n'
        return string

    def display_routes_string(self):
        string=""
        for route in self.routes:
            string+=str(route)
            string+='\n'
        return string




