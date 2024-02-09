from repository import Repo,File
from service import Service

class UI:
    def __init__(self,service):
        self.service= service

    def run(self):
        print("Welcome to the game")
        word = self.service.get_random_word()
        print("The word is: ", word)
        shuffle = self.service.shuffle(word)
        print("The shuffled word is: ", shuffle)
        count = self.service.get_score(word)
        wordlist= [char for char in word]
        print("The score is: ", count)
        while True:
            option=input("Please input option here >>")
            commands= option.split(" ")
            if commands[0]=="exit":
                return
            elif commands[0]=="swap":
                try:
                    self.service.save_history(shuffle)
                    if count>0 and shuffle!=word:
                        word1= int(commands[1])
                        #print(word1)
                        position1= int(commands[2])
                        #print(position1)
                        word2= int(commands[4])
                        #print(word2)
                        position2= int(commands[5])
                        #print(position2)
                        shuffle = self.service.swap(word1,position1,word2,position2,shuffle)
                        print("The shuffled word is: ",shuffle)
                        count-=1
                        print("The score is: ",count)
                        if count==0:
                            print("You have no more swaps")
                            return
                        if shuffle==wordlist:
                            print("You have won")
                            return
                except Exception as e:
                    print(e)

            elif commands[0]=="undo":
                try:
                    print(self.service.return_history())
                    shuffle= self.service.undo()
                    print("The shuffled word is: ",shuffle)
                    #count+=1
                    print("The score is: ",count)
                except Exception as e:
                    print(e)




