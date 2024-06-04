class Department:
    """
    A class to represent a Department.

    ...

    Attributes
    ----------
    name : str
        a formatted string to print out the name of the department
    sections : int
        an integer to represent the number of sections in the department
    students : list
        a list to store the number of students in each section

    Methods
    -------
    add_students(*students):
        Adds the number of students in each section.
    merge_Department(*departments):
        Merges the current department with other departments.
    """

    def __init__(self, name='ChE Department', sections=5):
        """
        Constructs all the necessary attributes for the Department object.

        Parameters
        ----------
            name : str
                a formatted string to print out the name of the department
            sections : int
                an integer to represent the number of sections in the department
        """

        self.name = name
        self.sections = sections
        self.students = []
        print(f'The {self.name} has {self.sections} sections.')

    def add_students(self, *students):
        """
        Adds the number of students in each section.

        Parameters
        ----------
            students : int
                an integer to represent the number of students in each section
        """

        if len(students) != self.sections:
            print(f'The {self.name} doesn\'t have {len(students)} sections.')
            return
        self.students = list(students)
        print(f'The {self.name} has an average of {sum(self.students)/self.sections} students in each section.')

    def merge_Department(self, *departments):
        """
        Merges the current department with other departments.

        Parameters
        ----------
            departments : Department
                Department objects to be merged with the current department
        """

        total_students = sum(self.students)
        total_sections = self.sections
        for department in departments:
            print(f'{department.name} is merged to {self.name}.')
            total_students += sum(department.students)
            total_sections += department.sections
        print(f'Now the {self.name} has an average of {total_students/total_sections} students in each section.')
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