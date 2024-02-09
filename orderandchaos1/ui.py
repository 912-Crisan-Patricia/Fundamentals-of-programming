from domain import Board,AI
from random import randint

class UI:

    @staticmethod
    def checkinteger(a):
        if a.isdigit():
            return int(a)
        else:
            return "Fals"

    def NewGame(self):
        b= Board()
        ai=AI()

        print(b)

        while b.gamewonplayer("o")==False and b.gamewonplayer("x")==False:
            ok=False
            while ok==False:
                l=input(" line>>")
                c=input(" column>>")
                piece= input("choose between x and o >>")
                if self.checkinteger(l)=="Fals":
                    print("Line not correct")
                if self.checkinteger(c)=="Fals":
                    print("Column not correct")
                if piece=="x" or piece=="o":
                    l=self.checkinteger(l)
                    c=self.checkinteger(c)
                    if c>=0 and c<6 and l<=5 and l>=0:
                        if b.data[l][c]==" ":
                            b.move(piece,l,c)
                            ok=True
                        else:
                            print("Invalid move, space not available")
                    else:
                        print("Move not within board")
                else:
                    print("Invalid piece, choose between x and o - case sensitive")
            print(b)

            if b.gamewonplayer("o")==True or b.gamewonplayer("x")==True:
                print("You win")
                break
            elif b.gamewoncomputer()==True:
                print("You lost")
                break

            print("Computer turn:")
            ai.move("x", "o", b)
            print(b)

            if b.gamewonplayer("o")==True or b.gamewonplayer("x")==True:
                print("You win")
                break
            elif b.gamewoncomputer()==True:
                print("You lost")
                break

            print("Want to save table?")
            decision=input("Type yes/no (case sensitive) >>")
            if decision== "yes":
                b.writetofile("table.txt")
                break
            else:
                break

            print("\n")

    def OldGame(self):
        b= Board()
        b.readfromfile("table.txt")
        ai=AI()

        print(b)
        while b.gamewonplayer("o")==False and b.gamewonplayer("x")==False:
            ok=False
            while ok==False:
                l=input(" line>>")
                c=input(" column>>")
                piece= input("choose between x and o >>")
                if self.checkinteger(l)=="Fals":
                    print("Line not correct")
                if self.checkinteger(c)=="Fals":
                    print("Column not correct")
                if piece=="x" or piece=="o":
                    l=self.checkinteger(l)
                    c=self.checkinteger(c)
                    if c>=0 and c<6 and l<=5 and l>=0:
                        if b.data[l][c]==" ":
                            b.move(piece,l,c)
                            ok=True
                        else:
                            print("Invalid move, space not available")
                    else:
                        print("Move not within board")
                else:
                    print("Invalid piece, choose between x and o - case sensitive")
            print(b)

            if b.gamewonplayer("o")==True or b.gamewonplayer("x")==True:
                print("You win")
                break
            elif b.gamewoncomputer()==True:
                print("You lost")
                break
            print("Computer turn")
            ai.move("x", "o", b)
            print(b)

            if b.gamewonplayer("o")==True or b.gamewonplayer("x")==True:
                print("You win")
                break
            elif b.gamewoncomputer()==True:
                print("You lost")
                break

            print("Want to save file?")
            decision=input("Type yes/no (case sensitive) >>")
            if decision== "yes":
                b.writetofile("table.txt")
                break
        print("\n")



    def start(self):
        while True:
            print("1.Start a new game \n")
            print("2.Continue an old one \n")
            print("3.Exit \n")

            command=int(input("Enter one of the options here >>"))
            if command==1:
                self.NewGame()
            elif command==2:
                self.OldGame()
            elif command==0:
                return
            else:
                command = input("Please type a valid command!")






