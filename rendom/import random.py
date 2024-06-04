import random
import datetime


def add_student():
    first_name = input("Enter the first name of the student: ")
    last_name = input("Enter the last name of the student: ")
    major = input("Select student's major (CE, EE, ET, ME, SE): ")

    if not first_name.isalpha() or not last_name.isalpha() or not first_name.istitle() or not last_name.istitle():
        print("Names should contain only letters and start with capital letters.")
        return

    current_year = datetime.datetime.now().year
    student_id = random.randint(10000, 99999)

    with open("students.txt", "a") as f:
        f.write(f"{student_id},{first_name},{last_name},{current_year},{major},{first_name.lower()}.{last_name.lower()}@lut.fi\n")
    
    print("Student added successfully!")


def search_student():
    search_term = input("Give at least 3 characters of the student's first or last name: ")
    if len(search_term) < 3:
        print("Search term should contain at least 3 characters.")
        return

    with open("students.txt", "r") as f:
        students = f.readlines()

    matching_students = [student for student in students if search_term in student]
    if matching_students:
        print("Matching students:")
        for student in matching_students:
            student_info = student.strip().split(",")
            student_id, first_name, last_name = student_info[0], student_info[1], student_info[2]
            print(f"ID: {student_id}, First name: {first_name}, Last name: {last_name}")
    else:
        print("No matching students found.")


def search_course():
    search_term = input("Give at least 3 characters of the course name or teacher's name: ")
    if len(search_term) < 3:
        print("Search term should contain at least 3 characters.")
        return

    with open("courses.txt", "r") as f:
        courses = f.readlines()

    matching_courses = [course for course in courses if search_term in course]
    if matching_courses:
        print("Matching courses:")
        for course in matching_courses:
            course_info = course.strip().split(",")
            course_id, course_name, credits, teachers = course_info[0], course_info[1], course_info[2], course_info[3]
            print(f"ID: {course_id}, Name: {course_name}, Teacher(s): {teachers}")
    else:
        print("No matching courses found.")


def add_course_completion():
    course_id = input("Give the course ID: ")
    student_id = input("Give the student ID: ")

    grade = input("Give the grade (1-5): ")
    if not grade.isdigit() or not (1 <= int(grade) <= 5):
        print("Grade is not a correct grade.")
        return

    date_str = input("Enter a date (DD/MM/YYYY): ")
    try:
        date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
        today = datetime.datetime.now()

        if date > today:
            print("Input date is later than today. Try again!")
            return

        if (today - date).days > 30:
            print("Input date is older than 30 days. Contact 'opinto'.")
            return
    except ValueError:
        print("Invalid date format. Use DD/MM/YYYY. Try again!")
        return

    with open("passed.txt", "r") as f:
        passed_courses = f.readlines()

    for i, line in enumerate(passed_courses):
        if line.startswith(course_id + "," + student_id):
            old_grade = int(line.strip().split(",")[-1])
            if int(grade) <= old_grade:
                print(f"Student has passed this course earlier with grade {old_grade}")
                return
            passed_courses[i] = f"{course_id},{student_id},{date_str},{grade}\n"
            with open("passed.txt", "w") as f:
                f.writelines(passed_courses)
            print("Record updated!")
            return

    with open("passed.txt", "a") as f:
        f.write(f"{course_id},{student_id},{date_str},{grade}\n")
    print("Record added!")


def show_student_record():
    student_id = input("Enter the student ID: ")

    with open("students.txt", "r") as f:
        students = f.readlines()
    
    student_info = [s.strip().split(",") for s in students if student_id in s][0]
    
    with open("passed.txt", "r") as f:
        passed_courses = f.readlines()

    with open("courses.txt", "r") as f:
        courses_info = f.readlines()

    student_courses = []
    total_credits = 0
    total_grade = 0

    for line in passed_courses:
        if line.startswith(student_id):
            course_id, date_str, grade = line.strip().split(",")[:3]
            total_grade += int(grade)
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            course_info = [c.strip().split(",") for c in courses_info if course_id in c][0]
            course_name, credits, teachers = course_info[1], course_info[2], course_info[3]
            student_courses.append((course_id, course_name, credits, date_str, teachers, grade))
            total_credits += int(credits)

    if student_info:
        print("Student ID:", student_id)
        print("Name:", student_info[1], student_info[2])
        print("Starting year:", student_info[3])
        print("Major:", student_info[4])
        print("Email:", student_info[5])

        if student_courses:
            print("Passed courses:")
            for course in student_courses:
                course_id, course_name, credits, date_str, teachers, grade = course
                print(f"Course ID: {course_id}, Name: {course_name}, Credits: {credits}, Date: {date_str}, Teacher(s): {teachers}, Grade: {grade}")

            average_grade = total_grade / len(student_courses)
            print(f"Total credits: {total_credits}, Average grade: {average_grade:.1f}")
        else:
            print("No passed courses.")
    else:
        print("Student not found.")


while True:
    print("You may select one of the following:")
    print("1) Add student")
    print("2) Search student")
    print("3) Search course")
    print("4) Add course completion")
    print("5) Show student's record")
    print("0) Exit")
    choice = input("What is your selection? ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        search_course()
    elif choice == "4":
        add_course_completion()
    elif choice == "5":
        show_student_record()
    elif choice == "0":
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please select a valid option.")
