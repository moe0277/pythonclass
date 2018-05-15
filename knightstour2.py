'''
Created on May 4, 2018

@author: mkhan
'''

import time
import random

class KnightsTour(object):
    '''
    classdocs
    '''


    def __init__(self, x=0, y=0):
        '''
        Constructor
        '''
        self.initBoard()
        self.initMoves()
        self.x = x
        self.y = y

    def initMoves(self):
        self.moves = []
        self.moves.append((2,1))
        self.moves.append((1,2))
        self.moves.append((-2,1))
        self.moves.append((-1,2))
        self.moves.append((-2,-1))
        self.moves.append((-1,-2))
        self.moves.append((2,-1))
        self.moves.append((1,-2)) 
        
    def initBoard(self):
        self.movecount = 0
        self.board = [[x * y for y in range(8)] for x in range(8)]

        for x in range(0,8):
            for y in range(0,8):
                self.board[x][y] = 0
            
    def __str__(self):
        res = ""
        res += "-----------------------------------------\n"
        for y in range(7, -1, -1):
            res += "| "
            for x in range(0, 8):
                res += str(self.board[x][y]).zfill(2) + " | "
            else:
                pass
            res += "\n"
        else:
            res += "-----------------------------------------" 
        return res
    
    def makeMove(self, x, y):
        self.movecount += 1
        self.x = self.x + x
        self.y = self.y + y
        self.board[self.x][self.y] = self.movecount
        
    def pickMove(self):
        validmoves = []
        for move in self.moves:
            newx = self.x + move[0]
            newy = self.y + move[1]
            if (newx >= 0) and (newx <=7) and (newy >= 0) and (newy <= 7) and self.board[newx][newy] == 0:
                validmoves.append(move) 
        if validmoves:
            return random.choice(validmoves)
        else:
            return (None, None)
    
    def tour(self):
        x,y = self.pickMove()
        while x:
            self.makeMove(x, y)        
            x, y = self.pickMove()
        
                
if __name__ == "__main__":
    print("Knights Tour2 v1.0")
    print()
    tourcounter = 0
    highest = 0
    kt = KnightsTour()
    start = time.time()
    initial = start
    while (kt.movecount < 64):
        tourcounter += 1
        kt.initBoard()
        kt.makeMove(0, 0)
        kt.tour()
        if kt.movecount > highest:
            highest = kt.movecount
        now = time.time()
        if (now % start) > 60:
            start = time.time() # reset
            print("Tours ran in last minute: %s" % tourcounter)
            print("Highest: %s" % highest)
            tourcounter = 0 # reset
    else: 
        print(kt)
        now = time.time()
        print("Solved in %s seconds" % str(now-initial))