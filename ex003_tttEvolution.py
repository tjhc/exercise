from ex001_ttt import *

class auto_ttt(ttt):

    autoWin = [[[ pp if (k//3, k%3) in w else ttt.e 
                 for k in range(9)]
                for w in ttt.win]
               for pp in ttt.p]

    def __init__(self):
        ttt.__init__(self)
        self.autoClear()

    def clearBoard(self):
        ttt.clearBoard(ttt)  

    def autoClear(self):
        """ clears autoBoard """
        self.autoBoard = [self.cp]+[self.e]*10

    def autoGet(self):
        """ get sting represention of board:
            pos0:   cp
            pos1-9: board in reading direction"""
        return "".join(self.autoBoard)

    def autoTurn(self, ind):
        """ sets board from string index"""
        self.autoBoard[ind] = self.cp
        self.cp = next(self.player)

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
        
        if self.autoBoard[1:] in self.autoWin[0]:
            res = self.p[0]
        elif self.autoBoard[1:] in self.autoWin[1]:
            res = self.p[1]
        elif autoBoard.count([self.e]) == 0:
            res = self.e
        else:
            res = False
        
        return res

    def turn(self, ind):
        self.auto2board(self)
        ttt.turn(ttt)
        self.board2auto(self)

    def checkWin(self):
        self.auto2board(self)
        ttt.checkWin(ttt)

    def checkEnd(self):
        self.auto2board(self)
        ttt.checkEnd(ttt)
        
        
        
