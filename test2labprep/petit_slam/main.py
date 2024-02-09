from repo import TextFileRepository
from service import PlayerService
from ui import UI

repository = TextFileRepository()
service = PlayerService(repository)
ui = UI(service)

ui.start_menu()