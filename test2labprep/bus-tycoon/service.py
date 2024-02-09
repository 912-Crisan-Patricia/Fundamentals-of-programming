from domain import Bus, Routes
from repo import *

class Service:
    def __init__(self,repo):
        self.repo=repo

    def getbuses(self):
        return self.repo.getbuses()

    def getroutes(self):
        return self.repo.getroutes()



    def displayBuses(self):
        return self.repo.display_buses_string()

    def displayRoutes(self):
        return self.repo.display_routes_string()

    def displayRouteBusses(self,route):
        if not self.repo.buses:
            raise Exception("No buses")
        list=[]
        for bus in self.repo.buses:
            if str(bus.getCode())==route:
                list.append(bus)
        if not list:
            raise Exception("No buses on this route")
        string=""
        for bus in list:
            string+=str(bus)
            string+='\n'
        return string


    '''
        Function that returns a string with the buses and their mileage
        input: -
        output: string
    '''
    def getBusMilage(self):

        b=self.repo.getbuses()
        r=self.repo.getroutes()
        tuple=[]
        for bus in b:
            for route in r:
                if str(route.getCode())==str(bus.getCode()):
                    mileage= int(route.getLength())* int(bus.getTime())
                    tuple.append((bus,mileage))
        string=""
        for t in tuple:
            string+=str(t[0])+" "+str(t[1])
            string+='\n'
        return string



    def displayBusesDescending(self):
        b=self.repo.getbuses()
        r=self.repo.getroutes()
        tuple=[]
        for route in r:
            mileage=0
            for bus in b:
                if str(route.getCode())==str(bus.getCode()):
                    mileage+= int(route.getLength())* int(bus.getTime())
            tuple.append((route,mileage))
        tuple.sort(reverse=True,key=lambda x:x[1])
        string=""
        for t in tuple:
            string+=str(t[0])+" "+str(t[1])
            string+='\n'
        return string





