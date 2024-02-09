
from ui import UI
from repo import Repo
from service import Service

repo=Repo("text.txt")
service=Service(repo)
ui=UI(service)

ui()

