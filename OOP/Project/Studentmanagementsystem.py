class Student:
    #constructor
    def __init__(self ,name ,roll,m1,m2):
        self.name = name
        self.roll = roll
        self.m1 = m1
        self.m2 = m2

    def accept(self,name, roll ,marks1,marks2):
        ob = Student(name, roll ,marks1,marks2)
        ls.append(ob)


    def display(self,ob):
        print("Name :",ob.name)
        print("Roll :",ob.roll)
        print("Marks :",ob.m1)
        print("Marks1 :",ob.m2)
        print("\n")

    def search(self,rn):
        for i in range(ls.__len__()):
            if (ls[i].roll == rn ):
                return i 
            
    def delete(self,rn):
        i = obj.search(rn)
        del ls[i]

    def update(self,rn,no):
        i = obj.search(rn)
        roll1 = no
        ls[i].roll = roll1
            

ls=[]
obj =Student("",0,0,0)
obj.accept("A",1,700,800)
obj.accept("B",2,700,3900)
obj.accept("C",3,600,3090)
obj.accept("D",4,500,3009)
print("\n")
print("List of student :\n ")

for i in range(ls.__len__()):
    obj.display(ls[i])
print("\nStudent Found")
s = obj.search(2)
obj.display(ls[s])

obj.delete(3)
print("\nStudent after Delete")
obj.update(2,6)
for i in range(ls.__len__()):
    obj.display(ls[i])


