class Car:
    def __init__(self,name,model):
        self.name=name #instance variable
        self.model_year=model
        self.wheel=4
    def view(self):    #instance method
        print("The model year of this",self.name,"is",self.model_year)
        print("It is a",self.wheel,"Wheel car")

#===========================
c1=Car("BMW",2023)
c2=Car("Audi",2024)
c1.view()
c2.view()