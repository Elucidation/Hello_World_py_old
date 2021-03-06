import random
import randomName
MAXENERGY = 50
BIRTHENERGY = int(MAXENERGY * 0.9)
#MAXLIFE = 100

class Creature:
    "It lives..."
    def __init__(self,name,x=0,y=0,energy=MAXENERGY,life=100):
        self.name = name
        self.x = x
        self.y = y
        self.birthday = -1
        self.deathday = -1
        self.energy = energy # if drops to zero is death
        self.life = int(life * (random.random()+0.3))
        self.maxlife = max(self.life,life)
        # This deteriorates at 1 per turn atm, uncertain
    def setBirth(self,time):
        self.birthday = time
    def changeEnergy(self,amount):
        self.energy += amount
        if self.energy < 0:
            self.energy = 0
        elif self.energy > MAXENERGY:
            self.energy = MAXENERGY
    def loseEnergy(self):
        "function of age"
        self.changeEnergy(-5)
        #self.changeEnergy(-(self.maxlife-self.life)/self.maxlife*10)
    def changeLife(self,amount):
        self.life += amount
        if self.life < 0:
            self.life = 0
        #elif self.life > MAXLIFE:
            #self.life = MAXLIFE
    def canGiveBirth(self):
        return self.energy >= BIRTHENERGY
    def getPos(self):
        return self.x,self.y
    def setPos(self,x,y):
        self.x=x
        self.y=y
    def giveBirth(self):
        self.changeEnergy(-BIRTHENERGY)
        babyname = randomName.randShortName()+self.name[-3:]
        bx = self.x + random.randrange(-10,10)
        by = self.y + random.randrange(-10,10)
        blife = self.maxlife
        baby=Creature(babyname,bx,by,life=blife)
        return baby

    def kill(self,time):
        #print self.name+" died at age "+`(time-self.birthday)`
        del(self)
    def isDead(self):
        return self.energy <= 0 or self.life <= 0
    def __str__(self):
        return self.name+ \
            "("+ \
            "L:"+`self.life`+","+\
            "E:"+`self.energy`+","+ \
            "P:(x:"+`self.x`+",y:"+`self.y`+")"+","+ \
            "Born:"+`self.birthday` +"," + \
            "ML:"+`self.maxlife`+\
            ")"


def randCreature():
    x = random.randrange(10,90)
    y = random.randrange(10,90)
    name = randomName.randShortName()
    bob = Creature(name,x,y)
    return bob
