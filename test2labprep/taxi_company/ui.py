

class UI:
    def __init__(self,service)-> None:
        self.service= service

    def __call__(self):
        while True:
            print("         MENU\n"
                  "1. Add adress\n"
                  "2. Display adress\n"
                  "3. Get addresses with smaller distance ")

            command=int(input(">>"))
            if command ==1:
                try:
                    id_input = input("Input id>>")
                    name_input =input("Input name>>")
                    number_input =input("Input number>>")
                    x_input =input("Input an coordinate>>")
                    y_input =input("Input an coordinate>>")
                    self.service.add_address(id_input,name_input,number_input,x_input,y_input)
                except Exception as e:
                    print(e)
            elif command==2:
                try:
                    addresses=self.service.get_addresses()
                    print(addresses)
                except Exception as e:
                    print(e)
            elif command==3:
                try:
                    distance=input("Input distance>>")
                    x=input("Input x>>")
                    y = input("Input y>>")
                    distances= self.service.get_distance(x,y,distance)
                    for a,d in distances:
                        print(str(a) + str(d)+'\n')
                except Exception as e:
                    print(e)




