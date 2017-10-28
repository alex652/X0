class Game:
    playerCount=0    
    
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.table={}


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

#alta var de metoda, nu mai itereaza pana la capat daca gaseste "-"
    def boardFull2(self):
        full=True
        i=0
        while i in range(self.size) and full==True:
            j=0
            while j in range (self.size) and full==True:
                if self.table[i,j]=="-":                    
                    full=False            
                j+=1
            i+=1    
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
                    
    #de vazut daca sunt corecte urmatoarele trei metode, si cum functioneaza
    def joinGame(self,Player,sign):
        self.player=Player
        Player.sign=sign
            
    def getCurentPlayer(self):
        return(self.player.name)

    def setCurrentPlayer(self,Player):
        self.player=Player
   
       
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

pla1=Player('John','x')
pla2=Player('Jim','0')
gm1.joinGame(pla1,'0')
gm1.joinGame(pla2,'x')



gm1.setCurrentPlayer(pla1) 
current_sign=pla1.sign

while not gm1.playerWon()["won"] and not gm1.boardFull():
    #add posibilty to quit while reading data
    gm1.displayBoard()
    #move=input( str(gm1.getCurentPlayer()) +' move (row column):')
    move=input('{0} move: <row column>:'. format(str(gm1.getCurentPlayer())))
    poz=Position(int(move[0]),int(move[2]))
    gm1.setCell(poz,current_sign)


    if gm1.getCurentPlayer()==pla1.name:
        gm1.setCurrentPlayer(pla2)
        current_sign=pla2.sign
    elif gm1.getCurentPlayer()==pla2.name:
        gm1.setCurrentPlayer(pla1)
        current_sign=pla1.sign  

print(" ")
gm1.displayBoard()

print("Won? : " +str(gm1.playerWon()["won"]))
    
