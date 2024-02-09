class Ui:
    def __init__(self,service):
        self.service=service

    def __call__(self):
        while True:
            print("         MENU\n"
                  "1. Display buses, routes\n"
                  "2. Display buses on certain route\n"
                  "3. Compute bus kilometers\n"
                  "4. Display buses in decending order for mileage\n")

            command=int(input(">>"))
            if command ==1:
                try:
                    routes = self.service.displayRoutes()
                    buses=self.service.displayBuses()
                    print(buses)
                    print(routes)
                except Exception as e:
                    print(e)

            elif command==2:
                try:
                    '''
                    list=self.service.getroutes()
                    string=""
                    for route in list:
                        string+=str(route)
                        string+='\n'
                    print(string)
                    list1=self.service.getbuses()
                    string=""
                    for bus in list1:
                        string+=str(bus)
                        string+='\n'
                    print(string)
                    '''
                    route=input("Input route>>")
                    buses=self.service.displayRouteBusses(route)
                    print(buses)
                except Exception as e:
                    print(e)
            elif command==3:
                try:
                    tuple=self.service.getBusMilage()
                    print(tuple)
                except Exception as e:
                    print(e)
            elif command==4:
                try:
                    routes=self.service.displayBusesDescending()
                    print(routes)
                except Exception as e:
                    print(e)
            else:
                print("Invalid command")


