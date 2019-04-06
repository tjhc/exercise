class ttt:
    """
tic tac toe class

Get current player with ttt.cp
Print board with str(ttt)
Play with turn method
Check for winning or game end with the respective methods
"""
    p = ["o", "x"]
    e = " "
    win  = [[(i,j) for i in range(3)] for j in range(3)]
    win += [[(i,j) for j in range(3)] for i in range(3)]
    win += [[(i,i) for i in range(3)]]
    win += [[(i,2-i) for i in range(3)]]

       
    def __init__(self):
        """ Initializes self
            creates empty self.board
            creates self.player generator""" 
        self.clearBoard()
        self.player = self.gen_player()
        self.cp = next(self.player)

    def clearBoard(self):
        """ initiates board with empty (self.e) symbols
            indexing: (row, column), origin top left (0,0)"""
        self.board = {(i,j) : self.e for i in range(3) for j in range(3)}

    def gen_player(self):
        """ player generator function
            yields alternating players"""
        while True:
            yield self.p[0]
            yield self.p[1]

    def checkWon(self):
        """ checks if current player has won the game (True/False)
            returns boolean"""
        won = False
        for w in self.win:
            won = won or 3 == [self.board[ind] for ind in w].count(self.cp)
        return won

    def checkEnd(self):
        """ checks if game ended in remis (True/False)
            returns boolean"""
        return list(self.board.values()).count(self.e) == 0 

    def turn(self, ind):
        """ current player sets mark at given position ind
            returns AssertionError for invalid position"""
        assert ind in self.board, "Invalid index"
        assert self.board[ind] == self.e, "Position already taken"
        self.board[ind] = self.cp
        self.cp = next(self.player)

    def __str__(self):
        """ returns string presentation of board"""
        return (f"\n"+5*"-"+f"\n").join("|".join(self.board[j,i]
                                                 for i in range(3))
                                        for j in range(3))
        
def manual_game():
    """ play tic tac toe in console
    input using numpad"""
    t = ttt()
    numBlock = { str(k+1): (2-k//3,k%3) for k in range(9)} 
    gameOn = True
    print(str(t))
    while gameOn:
        gameEnd = False
        cp = t.cp
        going = True
        while going:
            try:
                print(f"\nCurrently playing: {cp}")
                ind = input("Where would you liketo place your mark (input with numpad)?")
                assert ind in numBlock, "invalid position"
                ind = numBlock[ind]
                t.turn(cp, ind)
                print(str(t))
                if t.checkWon(cp):
                    print("Player", cp, "wins! Congratulations!")
                    gameEnd = True
                elif t.checkEnd():
                    print("No winner. Game ended in remis.")
                    gameEnd = True   
                going = False
            except AssertionError as e:
                print(e)

        if gameEnd:
            going = True
            while going:
                try:
                    again = input("Would you like to play again (y/n)?")
                    assert again in ["y","n"], "invalid input"
                    gameOn = again == "y"
                    if gameOn:
                        t.clearBoard()
                    print(str(t))
                    going = False
                except AssertionError as e:
                    print(e)
 

            
            
        
    
                
    
    
    
    
