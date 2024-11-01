class Dog:
    tricks = [] #Global will update for all

    def __init__(self,name):
        self.name = name
        self.tr = []  #local 

    def add_trick(self,trick):
        self.tricks.append(trick)

    def add_tr(self,tr2):
        self.tr.append(tr2)

d = Dog("ABC")
e = Dog("CBD")

d.add_trick("Roll over!")
print(d.tricks,e.tricks)

d.add_tr("a")
e.add_tr("b")
print(d.tr,e.tr)
