from domain import Assignments

class Repo:
    def __init__(self,path):
        self.path= path
        self.assignments=[]
        self.load_file()


    def add_assignments(self,assign):
        '''
        function checks if there are duplicates, ten adds it in list, savinf the file
        :param assign:
        :return:
        '''
        for assignment in self.assignments:
            if assignment== assign:
                raise ValueError("Assignment already in the file")
        self.assignments.append(assign)
        self.save_file()

    def load_file(self):
        with open(self.path,"r") as f:
            for line in f.readlines():
                line=line.strip()
                if line=="":
                    continue
                parts=line.split(",")
                assignment=Assignments(int(parts[0]),parts[1],parts[2])
                self.add_assignments(assignment)

    def save_file(self):
        with open(self.path,"w") as f:
            for assignment in self.assignments:
                f.write(str(assignment.get_id())+","+str(assignment.get_name())+","+str(assignment.get_solution()) +"\n")


    def display_assignments(self):
        return self.assignments



