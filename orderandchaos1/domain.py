from texttable import Texttable
import unittest
from unittest import TestCase
import random

class Board:

    def __init__(self):
        self.data=[[' ',' ',' ',' ',' ',' '] for x in range(6)]

    def __str__(self):
        self.table = Texttable()
        self.table.add_rows(self.data,[])
        return self.table.draw()

    def readfromfile(self,filename):
        with open(filename,"r") as f:
            lines=f.readlines()
            i=0
            print(type(lines))
            for line in lines:
                for j in range(6):
                    if line[j]=="+":
                        self.data[i][j]= " "
                    elif line[j]=="x":
                        self.data[i][j] = "x"
                    elif line[j]=="o":
                        self.data[i][j] = "o"
                i+=1

    def writetofile(self,filename):
        with open(filename,"w") as f:
            for line in self.data:
                for elem in line:
                    if elem==" ":
                        f.write("+")
                    elif elem=="x":
                        f.write("x")
                    elif elem=="o":
                        f.write("o")
                f.write("\n")

    def move(self,piece,row,col):
        self.data[row][col]=piece

    def gamewonplayer(self,piece):
        for i in range(6):
            if self.data[i][0]==self.data[i][1]==self.data[i][2]==self.data[i][3]==self.data[i][4]==piece:
                return True
            if self.data[i][1]==self.data[i][2]==self.data[i][3]==self.data[i][4]==self.data[i][5]==piece:
                return True
            if self.data[0][i]==self.data[1][i]==self.data[2][i]==self.data[3][i]==self.data[4][i]==piece:
                return True
            if self.data[5][i]==self.data[1][i]==self.data[2][i]==self.data[3][i]==self.data[4][i]==piece:
                return True
        for i in range(2):
            if self.data[i][i]==self.data[i+1][i+1]==self.data[i+2][i+2]==self.data[i+3][i+3]==self.data[i+4][i+4]==piece:
                return True

        if self.data[5][0]==self.data[4][1]==self.data[3][2]==self.data[2][3]==self.data[1][4]==piece:
            return True
        if self.data[0][5]==self.data[4][1]==self.data[3][2]==self.data[2][3]==self.data[1][4]==piece:
            return True
        if self.data[4][0] == self.data[3][1] == self.data[2][2] == self.data[1][3] == self.data[0][4] == piece:
            return True
        if self.data[5][1]==self.data[4][2]==self.data[3][3]==self.data[2][4]==self.data[1][5]==piece:
            return True

        if self.data[1][0]==self.data[2][1]==self.data[3][2]==self.data[4][3]==self.data[5][4]==piece:
            return True
        if self.data[4][5] == self.data[0][1] == self.data[1][2] == self.data[2][3] == self.data[3][4] == piece:
            return True


        return False

    def gamewoncomputer(self):
        for i in range(6):
            for j in range(6):
                if self.data[i][j]==" ":
                    return False
        return True

class AI:
    def checkforconnections(self,piece,board):
        #check vertical and horizontal
        for i in range(6):
            #horizontal
            if board.data[i][0]==board.data[i][1]==board.data[i][2]==board.data[i][3]==piece:
                if  board.data[i][4]==" ":
                    return i,4
            if board.data[i][4]==board.data[i][1]==board.data[i][2]==board.data[i][3]==piece:
                if board.data[i][0]==" ":
                    return i,5
                elif board.data[i][0]==" ":
                    return i,0
            if board.data[i][2]==board.data[i][3]==board.data[i][4]==board.data[i][5]==piece:
                if board.data[i][1]==" ":
                    return i,1
            #vertical
            if board.data[0][i]==board.data[1][i]==board.data[2][i]==board.data[3][i]==piece:
                    if board.data[4][i]==" ":
                        return 4,i
            if board.data[4][i]==board.data[1][i]==board.data[2][i]==board.data[3][i]==piece:
                    if board.data[1][i]==" ":
                        return 1,i
                    elif board.data[5][1]==" ":
                        return 5,i
            if board.data[5][i]==board.data[4][i]==board.data[2][i]==board.data[3][i]==piece:
                    if board.data[1][i]==" ":
                        return 1,i
        #check diagonal
        if board.data[0][0]==board.data[1][1]==board.data[2][2]==board.data[3][3]==piece:
            if board.data[4][4]==" ":
                return 4,4
        if board.data[4][4]==board.data[1][1]==board.data[2][2]==board.data[3][3]==piece:
            if board.data[5][5]==" ":
                return 5,5
            elif board.data[1][1]==" ":
                return 1,1
        if board.data[5][5]==board.data[4][4]==board.data[2][2]==board.data[3][3]==piece:
            if board.data[1][1]==" ":
                return 1,1
        if board.data[0][1]==board.data[1][2]==board.data[2][3]==board.data[3][4]==piece:
            if board.data[4][5]==" ":
                return 4,5
        if board.data[4][5]==board.data[1][2]==board.data[2][3]==board.data[3][4]==piece:
            if board.data[0][1]==" ":
                return 0,1
        if board.data[1][0]==board.data[2][1]==board.data[3][2]==board.data[4][3]==piece:
            if board.data[5][4]==" ":
                return 5,4
        if board.data[5][4]==board.data[2][1]==board.data[3][2]==board.data[4][3]==piece:
            if board.data[1][0]==" ":
                return 1,0

        #check diagonal2
        if board.data[5][0]==board.data[4][1]==board.data[3][2]==board.data[2][3]==piece:
            if board.data[1][4]==" ":
                return 1,4
        if board.data[1][4]==board.data[4][1]==board.data[3][2]==board.data[2][3]==piece:
            if board.data[0][5]==" ":
                return 0,5
            if board.data[5][0]==" ":
                return 5,0
        if board.data[0][5]==board.data[4][1]==board.data[3][2]==board.data[2][3]==piece:
            if board.data[5][0]==" ":
                return 5,0

        if board.data[0][4]==board.data[1][3]==board.data[3][2]==board.data[1][1]==piece:
            if board.data[4][0]==" ":
                return 4,0
        if board.data[4][0]==board.data[1][3]==board.data[3][2]==board.data[1][1]==piece:
            if board.data[0][4]==" ":
                return 0,4

        if board.data[5][1]==board.data[4][2]==board.data[3][3]==board.data[2][4]==piece:
            if board.data[1][5]==" ":
                return 1,5
        if board.data[1][5]==board.data[4][2]==board.data[3][3]==board.data[2][4]==piece:
            if board.data[5][1]==" ":
                return 5,1

        return False

    def move(self,piece1,piece2,board):
        if self.checkforconnections(piece1,board)==False:
            if self.checkforconnections(piece2,board)==False:
                ok=False
                while ok==False:
                    a=random.randint(0,5)
                    b=random.randint(0,5)
                    c=random.randint(1,2)
                    if board.data[a][b]==" ":
                        if c==1:
                            board.data[a][b]=piece1
                        else:
                            board.data[a][b] = piece1
                        ok=True
            else:
                a=self.checkforconnections(piece2,board)[0]
                b=self.checkforconnections(piece2,board)[1]
                board.data[a][b]=piece1 #put the other piece when 4 of same type
        else:
            a = self.checkforconnections(piece1, board)[0]
            b = self.checkforconnections(piece1, board)[1]
            board.data[a][b] = piece2


#tests
class Tests(TestCase):

    def testboard(self):
        b=Board()
        self.assertEqual(b.data[0][0]," ")
        self.assertEqual(b.data[5][5]," ")
        self.assertEqual(b.data[3][3]," ")
        assert b.gamewonplayer("x")==False
        assert b.gamewonplayer("o")==False

    def testai(self):
        b=Board()
        a=AI()

        b.data[0][0]="x"
        b.data[0][1]="x"
        b.data[0][2]="x"
        b.data[0][3]="x"
        assert a.checkforconnections("x",b)==(0,4)
        a.move("x","o",b)
        assert b.data[0][4]=="o"

if __name__ == '__main__':
   unittest.main()