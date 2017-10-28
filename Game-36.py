class Game:
    gameCount=0    
    
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.table={}
        self.playerCount=0


    def createBoard(self):            
        for a in range(self.size):
            for b in range(self.size):
                self.table[a,b]="-"
                
    def displayBoard(self):
        print("Table for game: {0}".format(self.name))
        print("")
        print("#########")
        for a in range(self.size):
            print("# ", end="")
            for b in range(self.size):                
                print(self.table[a,b]+ " " ,end="")
            print("#", end="")
            print("",end="\n")            
        print("#########")
        print("")

    
    def displayBoard2(self):
        #put all in a string, then print; to be added
        #display column and row numbers
         pass
        
    def setCell(self,Position,sign):
        if self.table[Position.row,Position.column]=="-":
            self.table[Position.row,Position.column]=sign


#vezi daca pot folosi ceva de genul:
#for element in mylist:
#    do_something(element)

    def boardFull(self):
        full=True
        for i in range(self.size):
            for j in range(self.size):
                #print (self.table[i,j])
                if self.table[i,j]=="-":
                    full=False                    
        return(full)
       
    def playerWon(self):
        winner={"won":False, "made":"nothing"}
        finished=False
        while winner["won"]==False and finished==False:
            i=j=0
            for i in range (self.size):
                self.count=1
                for j in range (1,self.size):
                    if self.table[i,0]==self.table[i,j] and self.table[i,0]!="-":
                        self.count+=1
                if self.count==self.size:
                    winner={"won":True, "made":"line"}
            if winner["won"]==True:
                break
            
            i=j=0
            for j in range (self.size):
                self.count=1
                for i in range (1,self.size):
                    if self.table[0,j]==self.table[i,j] and self.table[0,j]!="-":
                        self.count+=1
                if self.count==self.size:
                    winner={"won":True, "made":"colum"}
            if winner["won"]==True:
                break

            i=j=0
            self.count=1
            for i in range (1,self.size):                        
                if self.table[0,0]==self.table[i,i] and self.table[0,0]!="-":
                        self.count+=1
                if self.count==self.size:
                    winner={"won":True, "made":"diagonal1"}
            if winner["won"]==True:
                break
            
            i=j=0
            self.count=1
            for i in range (1,self.size):
                if self.table[0,self.size-1]==self.table[i,self.size-1-i] and self.table[0,self.size-1]!="-":
                        self.count+=1                        
                if self.count==self.size:
                    winner={"won":True, "made":"diagonal2"}
            if winner["won"]==True:
                break
            
            finished=True
        return (winner)                    
                    
    #de verificat daca sunt corecte urmatoarele patru metode
    def joinGame(self,player_inst,sign):
        self.current_player=player_inst
        player_inst.sign=sign
            
    def getCurrentPlayer(self):
        return(self.current_player.name)

    def getCurrentPlayer2(self):
        return(self.current_player)

    def setCurrentPlayer(self,player_inst):
        self.current_player=player_inst

    def switchTurns1(self):
        if gm1.getCurrentPlayer()==pla1.name:
            gm1.setCurrentPlayer(pla2)
            current_sign=pla2.sign
        elif gm1.getCurrentPlayer()==pla2.name:
            gm1.setCurrentPlayer(pla1)
            current_sign=pla1.sign

    def switchTurns2(self):
        if gm1.getCurrentPlayer2()==pla1:
            gm1.setCurrentPlayer(pla2)
            #current_sign=pla2.sign
        elif gm1.getCurrentPlayer2()==pla2:
            gm1.setCurrentPlayer(pla1)
            #current_sign=pla1.sign            
                      
    def switchTurns3(self,a,b):
        if current==a:
           current=b
        elif current==b:
           current=a

##    def readPlayers(self):
##        player_list=[]
##        order=['First','Second']
##        for i in range(2):
##            print(i)            
##            #p=Player(input('{0} player name: '.format(order[i])),input('Player sign: '))        
##            #player_list.append(p)
##            player_list.append(Player(input('{0} player name: '.format(order[i])),input('Player sign: ')))    
##              
##        return(player_list)  

    def readPlayerData(self):
        order=['First','Second']        
        self.playerCount+=1
        print (self.playerCount)
        self.playerData=[]
        self.playerData.extend((input('{0} player name: '.format(order[self.playerCount-1])),input('Player sign: ')))
        return(self.playerData)

       
class Player:
    def __init__(self,name,sign):
        self.name=name
        self.sign=sign

class Position:
    def __init__(self,row,column):
        self.row=row
        self.column=column
                    

gm1=Game('First_game',3)
gm1.createBoard()

#gm1.readPlayers()

data=gm1.readPlayerData()
pla1=Player(data[0],data[1])

data=gm1.readPlayerData()
pla2=Player(data[0],data[1])


#pla1=Player('John','x')
#pla2=Player('Jim','0')
#gm1.joinGame(pla1,'0')
#gm1.joinGame(pla2,'x')



gm1.setCurrentPlayer(pla1) 
#current_sign=pla1.sign
current_sign=gm1.getCurrentPlayer2().sign

while not gm1.playerWon()["won"] and not gm1.boardFull():
    #add posibilty to quit while reading data
    gm1.displayBoard()
    #move=input( str(gm1.getCurrentPlayer()) +' move (row column):')
    move=input('{0} move: <row column>:'. format(str(gm1.getCurrentPlayer2().name)))
    poz=Position(int(move[0]),int(move[2]))
#   gm1.setCell(poz,current_sign)
    gm1.setCell(poz,gm1.getCurrentPlayer2().sign)

    gm1.switchTurns2()

print(" ")
gm1.displayBoard()
gm1.switchTurns2()
print("{0} won. Made {1}.".format(gm1.getCurrentPlayer2().name,gm1.playerWon()["made"]))

    
