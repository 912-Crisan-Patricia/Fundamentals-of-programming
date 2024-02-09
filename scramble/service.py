from repository import Repo,File
import copy
import random
class Service:
    def __init__(self,repo):
        self.repo=repo

    def get_random_word(self):
        return self.repo.random()

    def return_history(self):
        return self.repo.return_history()

    def save_history(self, history):
        self.repo.save_history(copy.deepcopy(history))

    def undo(self):
        return self.repo.undo()


    def shuffle(self,sentence):
        '''
        This function shuffles the sentence
        :param sentence: the sentence to be shuffled
        :return: the shuffled sentence
        '''
        final=[]
        positions=[]
        toshuffle=[]
        for i in range(0,len(sentence)):
            if i==0 or i== len(sentence)-1:
                positions.append(i)
            elif i<len(sentence)-1 and (sentence[i]==' ' or sentence[i+1]==' ' or sentence[i-1]==' '):
                positions.append(i)
            else:
                toshuffle.append(sentence[i])

        random.shuffle(toshuffle)
        for i in range(0,len(sentence)):
            if i in positions:
                final.append(sentence[i])
            else:
                final.append(toshuffle.pop())

        return final

    def get_score(self,sentence):
        '''
        This function returns the score of the sentence
        :param sentence: the sentence to be scored
        :return: the score of the sentence
        '''
        count = 0
        for i in range(0,len(sentence)):
            if sentence[i]!=' ':
                count+=1
        return count

    def swap(self,word1, position1,word2,position2,shuffle):
        '''
        This function swaps 2 characters from the shuffled sentence based on word and position in that word
        :param word1: the word number of the first character
        :param position1: the position of the first character
        :param word2: the word number of the second character
        :param position2: the position of the second character
        :param shuffle: the shuffled sentence
        :return: the shuffled sentence with the 2 characters swapped
        '''
        positionchar1=0
        positionchar2=0
        numberofspaces=0

        if word1==0:
            positionchar1 = position1
        else:
            for i in range(0,len(shuffle)) :
                if shuffle[i]==' ':
                    numberofspaces+=1
                if numberofspaces==word1:
                    positionchar1=i+position1+1
                    break
        if word2==0:
            positionchar2 = position2
        else:
            numberofspaces=0
            for i in range(0,len(shuffle)) :
                if shuffle[i]==' ':
                    numberofspaces+=1
                if numberofspaces==word2:
                    positionchar2=i+position2+1
                    break

        shuffle[positionchar1],shuffle[positionchar2]=shuffle[positionchar2],shuffle[positionchar1]

        return shuffle







