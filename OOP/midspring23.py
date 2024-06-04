class Sphere:
    def __init__(self,a,r=1):
        self.v1=a
        self.r1=r
        self.color="White"

    def printDetails(self,*num):
        self.name=self.v1
        self.color="White"
        self.volume=(4/3)*3.1416*self.r1**3
        print(f"Sphere ID: {self.name} \nColor: {self.color} \nVolume: {self.volume}") 

    def merge_sphere(self,s1,s2):
        print("Spheres are being merged")
        self.r1=5
        self.printDetails(s1,s2)


        








sphere1 = Sphere("Sphere 1")
print("1***************")
sphere1.printDetails()
print("2***************")
sphere2 = Sphere("Sphere 2", 3)
print("3***************")
sphere2.printDetails()
print("4***************")
sphere3 = Sphere("Sphere 3", 2)
print("5***************")
sphere3.printDetails()
print("6***************")
sphere3.merge_sphere(sphere1,sphere2)
print("7***************")
sphere3.printDetails()
print("8***************")
sphere4 = Sphere("Sphere 4", 5, "Purple")
print("9***************")
sphere4.merge_sphere(sphere3)
print("10***************")
sphere4.printDetails()