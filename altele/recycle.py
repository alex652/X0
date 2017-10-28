##    def joinGame2(self,Player):
##        self.player2=Player
##        #self.sign2=sign
##        #Player.sign=sign

##    def joinGame(self, Game, sign):
##        self.game=Game    
##        self.sign=sign

gm2=Game('Second_game',3)

gm2.createBoard()

gm2.displayBoard()

print (pla1.sign, pla2.sign)
gm1.setCurrentPlayer(pla1)
print("currentPlayer: " +str (gm1.getCurentPlayer()))
gm1.setCurrentPlayer(pla2)
print("currentPlayer: " +str (gm1.getCurentPlayer()))


#print (gm1.getPlayers())
print(Position(1,1).row , Position(1,1).column)
#poz=Position(2,2)
#gm1.setCell(poz,"0")
print(pla2.name)


##poz=Position(0,0)
##gm1.setCell(poz,"0")
##poz=Position(0,1)
##gm1.setCell(poz,"0")
###poz=Position(0,2)
###gm1.setCell(poz,"0")
##
##
##poz=Position(1,0)
##gm1.setCell(poz,"x")
##poz=Position(1,1)
##gm1.setCell(poz,"x")

#rez=gm1.playerWon()


    #print("Full: " +str(gm1.boardFull2()))

