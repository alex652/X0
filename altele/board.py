size=3
table={}
for a in range(size):
        for b in range(size):
            table[a,b]="-"      
            
##def print_table (table):
##    for a in range(size):
##        for b in range(size):
##            print(table[a][b])
    
#create_table()

for a in range(size):
    for b in range(size):
        print(table[a,b] ,end="")
    print("",end="\n")

class Game:
    def __init__(self,name,size):
        self.name=name
        self.size=size
        

    def createBoard(self)    
        table={}
        for a in range(size):
            for b in range(size):
                table[a,b]="-"
                
    def displayBoard(self):
        for a in range(size):
            for b in range(size):
                print(table[a,b] ,end="")
            print("",end="\n")    
    
