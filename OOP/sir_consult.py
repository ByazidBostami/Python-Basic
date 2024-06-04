# Department
#    - dept name
#    - sections
#    - avg students
#    - init(0~2)
#    - add_students(*)
#    - merge_Department(*)

class Department:
    def __init__(self, a = "ChE Department",  b = 5):
        self.dep = a
        self.sec = b
        self.avg = 0
        print(f"The {a} has {b} sections.")

    def add_students(self, *num):
        if self.sec == len(num):
            s = 0
            for i in num:
                s += i
            self.avg = s / len(num)

            print(f"The {self.dep} has an average of {self.avg} students in each section.")
        else:
            print(f"The {self.dep} doesn't have {len(num)} sections.")

    def merge_Department(self, *objects):
        # find total student, with formula
        total_student = self.sec * self.avg
        out = ""
        for obj in objects:
            total_student += obj.sec * obj.avg
            out += f"{obj.dep} is merged to {self.dep}.\n"

        self.avg = total_student / self.sec
        out += f"Now the {self.dep} has an average of {self.avg} students in each section."
        return out

d1 = Department()
print('1-----------------------------')
d2 = Department('MME Department')
print('2-----------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------')
print(mega.merge_Department(d3))