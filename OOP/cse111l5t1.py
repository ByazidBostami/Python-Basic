class Student:
    def __init__(self,n,num):
        self.name=n
        self.__id=num #_student__id #private variable
        self.__details
    def getName(self):#get method #how we print private variable
        return self.__id   
    def setName(self,newId):#set method
        self.__id=newId
    def __details(self): #private method 
        print("Student er Jiboni")

#public,private
#driver code
s1=Student("Tanvir",1234)
s1.name="TanVir"
#s1.__id=2345
print(s1.name)
print(s1.__dict__)
#print(s1._student__id)
s1.setName(2345)
print(s1.getName())
print(s1.setName())