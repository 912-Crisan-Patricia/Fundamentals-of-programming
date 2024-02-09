from repository import TextFileRepository
from repository import TextFileRepositoryRoom
from service import Service
from ui import UI

reservations=TextFileRepository()
rooms=TextFileRepositoryRoom()

service=Service(rooms,reservations)
ui=UI(service)
UI.main(ui)