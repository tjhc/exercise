class ttt:
    p = ["o", "x"]
    e = " "
    win  = [[(i,j) for i in range(3)] for j in range(3)]
    win += [[(i,j) for j in range(3)] for i in range(3)]
    win += [[(i,i) for i in range(3)]]
    win += [[(i,2-i) for i in range(3)]]

       
    def __init__(self):
        self.clearBoard()
        self.player = self.gen_player()

    def clearBoard(self):
        self.board = {(i,j) : self.e for i in range(3) for j in range(3)}

    def gen_player(self):
        while True:
            yield self.p[0]
            yield self.p[1]

    def checkWon(self, cp):
        won = False
        for w in self.win:
            won = won or 3 == [self.board[ind] for ind in w].count(cp)
        return won

    def checkEnd(self):
        return list(self.board.values()).count(self.e) == 0 

    def turn(self, cp, ind):
        assert self.board[ind] == self.e, "Position already taken"
        self.board[ind] = cp

    def __str__(self):
        return (f"\n"+5*"-"+f"\n").join("|".join(self.board[j,i] for i in range(3))
                           for j in range(3))
        
def game():
    t = ttt()
    numBlock = { str(k+1): (2-k//3,k%3) for k in range(9)} 
    gameOn = True
    print(str(t))
    while gameOn:
        gameEnd = False
        cp = next(t.player)
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
 
            
            
            
        
    
                
    
    
    
    
