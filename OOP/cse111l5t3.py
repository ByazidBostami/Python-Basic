class Spaceship:
    def __init__(self,n,c):
        self.name=n
        self.capacity=c
        self.cargos=[]
        self.capacityCount=0

    def load_cargo(self,c1):
        if c1.__weight+self.capacityCount<self.capacity:
            self.cargos.append(c1.__name)
            self.capacityCount+=c1.getWeight()


        


class Cargo:
    def __init__(self,n,w):
        self.__name=n
        self.__weight=w

    def getName(self):
        return self.__name
    def getWeight(self):
        return self.__weight    
        
