from domain import Player
from repo import *
import random

class Service:
    def __init__(self,repo):
        self.repo=repo
        self.pairs=[]

    def get_players(self):
        return self.repo.players_as_string()

    def powers_of_two(self,l):
        '''

        :param l: length in terms of powers of 2
        :return:
        '''
        powers=[]
        i=1
        while i<=l:
            if i& l: powers.append(i)
            i<<=1
        return powers


    def quali(self):
        '''
        Function checks if there is need for a qualiifcation round
        :return: true if no/false otherwise
        '''
        players=len(self.repo.players)
        return players !=0 and players&(players-1)==0

    def qualifications(self):
        '''
        Function computes players for qualification
        :return:
        '''
        length=(len(self.repo.players))
        p=self.powers_of_two(length)
        rounds=length- p[-1]
        nr_players= 2*rounds
        start=length- nr_players
        qplayers=[]
        for i in range(start,len(self.repo.players)):
            qplayers.append(self.repo.players[i])
            return qplayers

    def pairs(self,players_list):
        '''
        Function pairs the players radomly
        :param players_list:
        :return:
        '''
        ok=0
        chosen=[]
        while ok !=2:
            player=players_list[random.randint(0,len(players_list))-1]
            if player not in self.pairs:
                chosen.append(player)
                ok+=1
        return chosen

    def sort_players(self):
        self.repo.players.sort(reverse=True,key=lambda x:x.strength)
