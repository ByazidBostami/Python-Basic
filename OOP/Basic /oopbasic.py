class Student:
    def __init__(self,name,id,semester):
        self.name = name
        self.id = id
        self.semester = semester
        self.cgpa = 0.00

    def __str__(self): # this will called for one line print 
        return "The student name id {} his id {} and he is in {}".format(self.name,self.id,self.semester)
    
    def update_cgpa(self,cg):
        if cg > self.cgpa:
            self.cgpa = cg
        else:
            print("Cgpa should not be lower then previous one")

    def __eq__(self, value): # For checking equality
        return self.name == value.name and self.cgpa == value.cgpa 

    


s1= Student("Byazid",23101498,"5th")
s2 = Student("Fairoz Maliha",23101495,"5th")
s3 = Student("Suvo",23405,"5th")
s4 = Student("Suvo",23405,"5th")
print(s1.name)

print(s2)

s2.update_cgpa(3.75)
#print(s2.cgpa)
s2.update_cgpa(2.75)
print(s2.cgpa)
print(s3 == s4)