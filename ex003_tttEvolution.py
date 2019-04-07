from ex001_ttt import *
from random import choices as choose

class auto_ttt(ttt):

    autoWin = [[ k for k in range(9)
                 if ((k//3, k%3) in w)]
               for w in ttt.win]

    def __init__(self):
        ttt.__init__(self)
        self.autoClear()

    def autoClear(self):
        """ clears autoBoard """
        self.autoBoard = [self.cp]+[self.e]*9

    def autoGet(self):
        """ get sting represention of board:
            pos0:   cp
            pos1-9: board in reading direction"""
        return "".join(self.autoBoard)

    def autoTurn(self, ind):
        """ sets board from string index"""
        self.autoBoard[ind] = self.cp
        self.cp = next(self.player)
        self.autoBoard[0] = self.cp

    def auto2board(self):
        """ synchronizes autoBoard to board"""
        self.board = { (k//3, k%3): v
                       for k, v in enumerate(self.autoBoard[1:]) }

    def board2auto(self):
        """ synchronized board to autoBoard"""
        self.autoBoard = [self.cp]+[self.board[k//3,k%3]
                                    for k in range(9)]

    def autoEnd(self):
        """ checks for end
            return: ongoing -> False
                    winner -> winner
                    remis -> self.e """
        ab = self.autoBoard
        aw = self.autoWin
        
        # standard: game not ended 
        res = False
        
        # check for filled board
        if ab.count(self.e) == 0:        
            res = self.e
            
        # check for winner 
        for lines in aw:
            for p in self.p:
                if [ab[i+1] for i in lines].count(p)==3:
                    res = p
        
        return res

    def turn(self, ind):
        self.auto2board()
        ttt.turn(self, ind)
        self.board2auto()

    def checkWin(self):
        self.auto2board(self)
        ttt.checkWin()

    def checkEnd(self):
        self.auto2board(self)
        ttt.checkEnd()

    def __str__(self):
        self.auto2board()
        
        
class ttt_ai:

    def __init__(self):

        # key: sequence
        # value: possible inputs, rating (start 1, win +3, remis 1, lose 0) 
        self.knowledge = dict()

    def setGame(self, game):
        self.game = game

    def setRound(self):
        # key: sequence
        # value: taken input
        self.roundKnow = dict()

    def createKnowledge(self, seq):
        self.knowledge[seq] = {i+1:1 for i,v in enumerate(seq[1:]) if v == self.game.e}

    def play(self):
        seq = self.game.autoGet()
        self.cp = seq[0]
        if not seq in self.knowledge:
            self.createKnowledge(seq)
        k = self.knowledge[seq]
        ind = choose(list(k.keys()), list(k.values()))
        ind = ind[0]
        self.roundKnow[seq] = ind
        self.game.autoTurn(ind)

    def reflect(self, result):
        if result == self.game.e:
            inc = 1
        elif result == self.cp:
            inc = 3
        else:
            inc = 0

        if inc>0:            
            for (seq,ind) in self.roundKnow.items():
                self.knowledge[seq][ind] += inc

    def merge(self, ttt_ai2):
        for (seq, val) in ttt_ai2.knowledge.items():
            if seq in self.knowledge:
                for ind in self.knowledge[seq]:
                    self.knowledge[seq][ind] += val[ind]
            else:
                self.knowledge[seq] = val
                    
        

def learn(n, p1=None, p2=None):
    if p1==None:
        p1 = ttt_ai()
    if p2==None:
        p2 = ttt_ai()
        
    game = auto_ttt()
    p1.setGame(game)
    p2.setGame(game)

    def gen(p1, p2):
        while True:
            yield p1
            yield p2

    gp = gen(p1,p2)

    
    for i in range(n):
        p1.setRound()
        p2.setRound()
        game.autoClear()
        result = game.autoEnd()
        while result == False:
            p = next(gp)
            p.play()
            game.auto2board()
            result = game.autoEnd()
        p1.reflect(result)
        p2.reflect(result)
    p1.merge(p2)
    p2 = None
    return p1

        
        
        
        
            
        
        
