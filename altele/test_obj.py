import urllib.request

class game:
    
    def __init__(self,name):
        self.name=name    

class player:
    age=0
    def __init__(self,name):
        self.name=name
        player.age+=1

    def joinGame(self,game_inst):
        self.game_inst=game_inst

    def getGame(self):
        return (self.game_inst)

    def setAge(self,age):
        self.age=age
                


p1=player("John")
p2=player("Jim")

g1=game("First_round")
g2=game("Second_round")

p1.joinGame(g1)
p1.joinGame(g2)

rez=p1.getGame()

p1.setAge(15)
p2.setAge(16)

print(rez.name)
print(p1.age)
p2.setAge(16)
print(p1.age)
print(p2.age)
print(player.age)

with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()

