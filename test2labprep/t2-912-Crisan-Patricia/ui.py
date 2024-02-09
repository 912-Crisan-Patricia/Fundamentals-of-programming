class Ui:
    def __init__(self,service):
        self.service=service

    def __call__(self):
        while True:
            print("     Menu \n"
                  "1.Add assignment\n"
                  "2.Display assignments\n"
                  "3.Dishonesty check\n")

            command=int(input("Please input command>>"))

            if command==1:
                try:
                    id=input("Please input id>>")
                    name=input("Please input name>>")
                    solution=input("Please input solution>>")

                    self.service.add_assignment(id,name,solution)

                except Exception as e:
                    print(e)
            elif command==2:
                try:
                    list= self.service.display_assignments_as_string()
                    print(list)
                except Exception as e:
                    print(e)
            elif command==3:
                return
            else:
                return



