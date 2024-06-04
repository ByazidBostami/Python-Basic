#Task1
class Student:
    
    def __init__(self, name, cgpa, credit=9, department="CSE"):

        self.name = name
        self.cgpa = cgpa
        self.credit = credit
        self.department = department
        self.scholarship_status = "No scholarship"

    def checkScholarshipEligibility(self):

        if self.cgpa >= 3.7 and self.credit > 10:
            self.scholarship_status = "Merit-based scholarship"
            print(f"{self.name} is eligible for Merit-based scholarship.")
        elif self.cgpa >= 3.5 and self.credit > 10:
            self.scholarship_status = "Need-based scholarship"
            print(f"{self.name} is eligible for Need-based scholarship.")
        elif self.cgpa >= 3.5 and self.credit < 10:
            self.scholarship_status = "No scholarship"
            print(f"{self.name} is eligible for No scholarship.")
        else:
            print(f"{self.name} is not eligible for scholarship.")

    def showDetails(self):
        
        print(f"Name: {self.name} \nDepartment: {self.department} \nCGPA: {self.cgpa} \nNumber of Credits: {self.credit} \nScholarship Status: {self.scholarship_status}")
print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()
