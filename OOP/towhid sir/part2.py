class Fish:
    def __init__(self,name): #constructor
        self.name=name
    def method1(self):
        print("Class Method is Working")

#========================================
f1=Fish("Hilsha")
f1.method1()