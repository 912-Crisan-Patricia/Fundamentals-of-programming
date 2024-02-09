from repository import Repo,File
from service import Service

class UI:
    def __init__(self,service):
        self.service= service

    def run(self):
        while True:
            print(" 1. Add sentence \n")
            print(" 2. Play game \n")

            option=int(input(" >>"))
            if option==1:
                sentence= input("Add sentence here >>")
                self.service.add(sentence)
            elif option==2:
                x=0
                h= ['h','a','n','g','m','a','n']
                sentence= self.service.get_random()
                display = self.service.partialdisplay(sentence)
                print(display)
                while x<7 and '_' in display:
                    letter= input("Input a word >>")
                    aux_display= display
                    new_display= self.service.play(letter,display,sentence)
                    if aux_display==new_display :
                        x+=1
                    y= self.service.tries(x)
                    print(y)
                    print(display)
                if x==7:
                   print("You lost")
                   return
                elif "_" not in display:
                    print("You win")
                    return
            else:
                print("Invalid option")