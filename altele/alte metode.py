
def readPlayers2(self):
    for i,p in zip(['First', 'Second'],['pla1','pla2']):
    p=Player(input('{0} player name: '.format(i)),input('Player sign: '))


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
