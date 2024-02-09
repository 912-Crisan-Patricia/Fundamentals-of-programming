import random

class Repo:
    def __init__(self):
        self.sentences= []

    def add(self,sentence):
        '''
        Adds a sentence to the list
        :param sentence: char
        :return: -
        '''
        for i in self.sentences:
            if i==sentence:
                raise ValueError("Sentence already in file")
        self.sentences.append(sentence)


    def get_all(self):
        '''
        Returns all the sentences from the list
        :return: list of sentences
        '''
        return self.sentences


    def randomsentence(self):
        '''
        Returns a random sentence from the list
        :return: sentence from the list
        '''
        return random.choice(self.sentences)

class File(Repo):
    def __init__(self):
        super().__init__()
        self.load()


    def load(self):
        '''
        Loads the sentences from the file
        :return: -
        '''
        with open("sentences.txt","r") as f:
            self.sentences= [line.strip() for line in f.readlines()]


    def save(self):
        '''
        Saves the sentences to the file
        :return: -
        '''
        with open("sentences.txt","w") as f:
            for i in self.sentences:
                f.write(i)
                f.write("\n")

    def add(self,s):
        '''
        Adds a sentence to the list and saves it to the file
        :param s: sentence char
        :return: -
        '''
        super().add(s)
        self.save()
