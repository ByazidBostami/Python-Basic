class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def update_color(self,color):
        self.color=color
    def view(self):
        print(self.color,self.name,"is smiling")
#==============================
        
d1=Dog("Rover","Brown")
d2=Dog("Tomy","White")
d1.view()
d1.update_color("Black")#Update color
d1.view()
d2.view()
d2.update_color("Red")
d2.view()
print(d1.__dict__) 
print(dir(d2))