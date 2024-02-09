import random

class Repo:
    def __init__(self):
        self.sentences=[]
        self.history=[]

    def random(self):
        return random.choice(self.sentences)

    def get_all(self):
        return self.sentences

    def save_history(self,sentence):
        self.history.append(sentence)

    def return_history(self):
        return self.history


    def undo(self):
        if len(self.history)==0:
            raise ValueError("No more undos")
        return self.history.pop()


class File(Repo):
    def __init__(self):
        super().__init__()
        self.load()

    def load(self):
        with open("input.txt","r") as f:
            self.sentences=[line.strip() for line in f.readlines()]

