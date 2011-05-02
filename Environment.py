import random

class Environment:
    "Where Creatures live, 2D plane 100x100 units starting from 0,0"
    def __init__(self):
        self.MAXWIDTH = 100
        self.MAXHEIGHT = 100
        self.creatures = []
        self.time = 0

    def addCreature(self,creature):
        creature.setBirth(self.time)
        creature.setPos(*self.clampPos(*creature.getPos()))
        self.creatures.append(creature)
    def clampPos(self,x,y):
        return max(0,min(x,self.MAXWIDTH)), max(0,min(y,self.MAXHEIGHT))
    def removeCreature(self,creature):
        self.creatures.remove(creature)
        creature.kill(self.time)
        
    def step(self):
        self.time += 1
        self.printStatus()
        print "----- Stepping -----"
        for c in self.creatures:
            c.changeEnergy(-5) # slow energy loss
            c.changeLife(-1) # Aging
            if (c.x > self.MAXWIDTH/2):
                c.changeEnergy(10) # Right half gets sunlight
        self.removeDead()

        # Babymaking time
        for c in self.creatures:
            if c.canGiveBirth():
                if len(self.creatures) < 10: # hardcoded for now
                    self.addCreature(c.giveBirth())
            

    def removeDead(self):
        for c in self.creatures:
            #print "Checking if ",c," is dead... ",c.isDead()
            if c.isDead():
                self.removeCreature(c)

    def printStatus(self):
        print "------ Environment ------"
        print " Time: ", self.time, " units"
        print " Population Count: ", len(self.creatures)
        for c in self.creatures:
            print c


