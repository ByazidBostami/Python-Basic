"""Class object Constructor attributes methods()"""
class Student:

    def __init__(self,name,Id):
        self.name=name #instance variable
        self.id=Id   #instance variable #we should call with instance variable 
       #print("A student object created") #যত বার অবজেক্ট ক্রিয়েট হবে তত গুলো প্রিন্ট হবে 
        #print(self)
        print(name) #thi is how we print al instance element
#----------------
#variable=class_name()
s1=Student("Byazid",23101498) # how we create object variable =class_name 
s2=Student("Rendom",23101499)
s1.id=23101497 #how we change the id 
print(s1.name)
#print(s1)