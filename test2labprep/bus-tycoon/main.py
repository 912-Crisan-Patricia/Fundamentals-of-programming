from repo import Repo
from service import Service
from ui import Ui

repo=Repo("routes.txt","buses.txt")
service=Service(repo)
ui=Ui(service)

ui()
