class Cat:
    def __init__(self,color,action):
        self.color=color
        self.action=action
    
    def view(self,num,clr):
        num=num+5
        clr1=clr
        clr1[0]="Green"
        print("Method inside:",num)
        print("Method inside:",clr1)
colors=["Black","Red","Yellow","Blue"]
c1=Cat("White","Jumping")
x=55
c1.view(x,colors) #pass by ref
print("Method Outsite",x)
print("Method Outside",colors)