from ui import UI
from repository import File,Repo
from service import Service

repo=File()
service= Service(repo)
ui=UI(service)


ui.run()

'''
anna has apples
patricia has pears
cars are fast
planes are quick
the quick brown fox jumps over the lazy dog
'''

