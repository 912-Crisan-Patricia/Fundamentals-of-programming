class Assignments:
    def __init__(self, id, name, solution):
        self.id=id
        self.name=name
        self.solution=solution

    #getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_solution(self):
        return self.solution

    def __str__(self):
        return str(self.id)+","+str(self.name)+","+str(self.solution)



