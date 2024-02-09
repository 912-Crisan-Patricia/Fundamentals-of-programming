from domain import Assignments
from repo import *


class Service:
    def __init__(self,repo):
        self.repo= repo


    def add_assignment(self,id, name,solution):
        '''
        Function checks if user inputs are correct, then adds it to the repo
        :param id:
        :param name:
        :param solution:
        :return:
        '''
        if not id.isdigit():
            raise ValueError("id not an integer")
        list= self.repo.assignments
        for a in list:
            if str(a.get_id())== id:
                raise ValueError("Id not unique")
        if len(name) <3:
            raise ValueError("Name too short")
        if not solution:
            raise ValueError("Solution empty")

        assign=Assignments(id,name,solution)
        self.repo.add_assignments(assign)


    def display_assignments_as_string(self):

        list=self.repo.assignments
        string=""
        for assign in list:
            string+=str(assign)+"\n"
        return string

'''

    def dishonesty(self):

        list= self.repo.assignments

        for a in list:
            for b in list:
                if a!=b:
                    show_a=0
                    show_b=0
                    dishonesty=0
                    a_split= a.split(" ")
                    a_len=len(a_split)
                    b_split=b.split(" ")
                    b_len=len(b_split)

                    if a_len> b_len:
                        l=a_len
                        show_a=1
                    else:
                        l=b_len
                        show_b=1
                    for i in range(0,l):
                        if a_split[i]==b_split[i]:
                            dishonesty+=1

                    if dishonesty > l//5:
                        if(show_a==1):
                            print(str(b.get_name())+"->"+str(a.get_name())+"("+str(dishonesty)+") of "+str(a.get_name())+"solution"+"\n")
'''





