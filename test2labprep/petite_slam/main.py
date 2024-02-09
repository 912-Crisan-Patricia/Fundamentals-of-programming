from ui import Ui
from service import Service
from repo import Repo


repo=Repo("text.txt")
service=Service(repo)
ui=Ui(service)

ui()