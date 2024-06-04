class House:
    def __init__(self): #constructor
        self.window=4 #instan
        self.door=2
    def view(self):
        print(self.window,"windows",self.door,"doors")

#======================
h1=House()
h2=House()
h1.window=6 #update value
h2.door=3
h1.view()
h2.view()