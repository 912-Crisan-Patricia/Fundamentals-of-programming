class Ui:
    def __init__(self,service):
        self.service=service

    def qualification(self):
        print("Q\n")
        new_players=self.service.qualifications()
        winners=[]
        length=len(new_players)//2
        while length!=0:
            pairs= self.service.pairs(new_players)
            for player in pairs:
                print(str(player))
            winner=

    def __call__(self):
        while True:
            print ("        MENU \n"
                   "1. Display players \n"
                   "2. Quali round\n"
                   "3. Tournament\n")
            command= int(input("Give command>>"))
            if command==1:
                try:
                    players=self.service.get_players()
                    print(players)
                except Exception as e:
                    print(e)
            if command==2:
                try:
                    if self.service.quali()==True:
                        print("There is no need for qualification")
                    else:
                        self.qualification()
                except Exception as e:
                    print(e)