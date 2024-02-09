from repository import Repo,File

class Service(object):
    def __init__(self,repo):
       self.repo= repo

    def add(self,sentence):
        '''
        Add a sentence to the repository
        :param sentence: string
        :return: -
        '''
        if len(sentence)<1 or sentence=="" :
            raise ValueError("Invalid sentence, too short")
        for i in sentence.split():
            if len(i) < 3:
                raise ValueError("Invalid sentence, words short")
        self.repo.add(sentence)

    def get_random(self):
        '''
        Get a random sentence from the repository
        :return: string
        '''
        return self.repo.randomsentence()

    def partialdisplay(self,sentence):
        '''
        Create a partial display of the sentence, with the first and last letters and the letters that are between spaces
        :param sentence: string before the display
        :return: list
        '''
        letters =['_',' ']
        display= []
        for i in range(0, len(sentence)):
            if i==0 or i== len(sentence)-1:
                if sentence[i] not in letters:
                    letters.append(sentence[i])
            if i< len(sentence)-1 and (sentence[i-1]==' ' or sentence[i+1]==' '):
                if sentence[i] not in letters:
                    letters.append(sentence[i])

        for i in sentence:
            if i in letters:
                display.append(i)
            else:
                display.append('_')

        return display

    def play(self,word, display,sentence):
        '''
        Play a word in the sentence
        :param word: char top be verified in the sentence
        :param display: list of the display
        :param sentence: string to be compared to
        :return:
        '''
        for i in range(0,len(sentence)):
            if word==sentence[i]:
                display[i]= word
        return display

    def tries(self,x):
        '''
        Create a string with the number of tries and displays it
        :param x: chars to be displayed from the string h
        :return: string with the number of tries
        '''
        h = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        s=""
        for i in range(0,x):
            s+=(h[i])
        return s








