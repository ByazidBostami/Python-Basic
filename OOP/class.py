class car:  #this is how we declare a class 
    def __init__(self): 
        self.brand="Car Brand"
        self.model="Car Model"
        self.licence="XYZ"
        self.engine_cap=1200
        self.seats=5
    
    def printDetails(self): #this is how we print our class element 
        print("---")
        print(self.brand)
        print(self.model)
        print(self.licence)
        print(self.engine_cap)
        print(self.seats)

c1=car() #define the class
print(c1)#print the class(type)
print(c1.brand) #print individula element 
c1.brand="BMW"
print("--")
print(c1.brand)
print(c1.printDetails())