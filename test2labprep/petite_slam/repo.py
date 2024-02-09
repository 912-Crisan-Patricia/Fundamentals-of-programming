from domain import Player

class Repo:
    def __init__(self,path):
        self.path=path
        self.players=[]
        self.load_file()

    def set_player(self,value):
        self.players=value

    def __getitem__(self, item):
        return self.players[item]

    def get_player_by_id(self, player_id):
        player_exists = False
        for player in self.players:
            if player.player_id == player_id:
                player_exists = True

        if player_exists:
            return player
        else:
            return False

    def add_player(self, player):
        self._players.append(player)

    def __len__(self):
        return len(self._players)

    def load_file(self):
        with open(self.path, "r") as f:
            for line in f:
                tokens=line.split(",")
                self.players.append(Player(int(tokens[0]),tokens[1],int(tokens[2])))

    def save_file(self):
        with open(self.path, "w") as f:
            for player in self.players:
                string= str(player.get_id())+","+str(player.get_name())+","+str(player.get_power())+"\n"
                f.write(string)

    def players_as_string(self):
        string=""
        for player in self.players:
            string+=str(player)
            string+="\n"
        return string

    def get_players(self):
        return self.players



