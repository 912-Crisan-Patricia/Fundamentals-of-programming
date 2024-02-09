
from repo import Repo
from service import Service
from ui import Ui

repo=Repo("assignments.txt")
service=Service(repo)
ui=Ui(service)

ui()

'''
1,Anna,I will make sure to implement a layered architecture solution
2,John,The program is layered
3,Betty,I did not understand architecture
4,Vlad, My proposed solution does not include layers
'''

