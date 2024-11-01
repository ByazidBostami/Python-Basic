class Animale:
    
    def __init__(self,name):
        self.name =name

    def walk(self):
        print(f"{self.name} is walking")
    
    def eat(self):
        print("{} is eating".format(self.name))


class Cat(Animale):

    def eat(self):
        print("I dont eating now")

class Dog(Cat):
    dname = "Good dog "
    def eat(self):
        print(f"{self.name} dont bite" )

class crocodile(Dog):
    pass

    

a = Animale("Cow")
b = Cat("Nawee")

a.eat()
a.walk()

b.walk()
b.eat()
b1 = Dog("Hua")
b1.eat()
print(b1.dname)

c1 = crocodile("halum")
c1.eat()

