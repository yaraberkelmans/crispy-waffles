class Student():
    def __init__(self, student_id, courses):
        self.student_id = student_id
        self.courses = courses


class Course():
    def __init__(self, course_name, lectures_n, tutorial_n, tutorial_cap, labs_n, labs_cap, e_students):
        self.course_name = course_name
        self.lectures_n = lectures_n
        self.tutorial_n = tutorial_n
        self.tutorial_cap = tutorial_cap
        self.labs_n = labs_n
        self.labs_cap = labs_cap
        self.e_students = e_students

        if int(self.tutorial_n) >= 1:
            self.tutorials = {}
        if int(self.labs_n) >= 1:
            self.labs = {}

    def add_students_tut(self, student_list):
        """This method adds a certain list of students to seperate tutorial groups, based on the tutorials_cap per tutorial group. The tutorials are in a dictionary with the 
        tutorial # as key and a list of students as values"""
        tut_amount = len(student_list)// int(self.tutorial_cap)
        if len(student_list) % int(self.tutorial_cap) > 0:
            tut_amount += 1
        for x in range(1,tut_amount+1):
            stud_per_tut = len(student_list)/ tut_amount
            self.tutorials[x] = student_list[round(((x-1) * stud_per_tut)):round((x *stud_per_tut))]
        print(len(self.tutorials.keys()))

    def add_students_lab(self, student_list):
        """This method adds a certain list of students to seperate lab groups, based on the labs_cap per lab group. The labs are in a dictionary with the 
        lab # as key and a list of students as values"""
        lab_amount = len(student_list)// int(self.labs_cap)
        if len(student_list) % int(self.labs_cap) > 0:
            lab_amount += 1
        for x in range(1,lab_amount+1):
            stud_per_lab = len(student_list)/ lab_amount
            self.labs[x] = student_list[round(((x-1) * stud_per_lab)):round((x *stud_per_lab))]
        print(len(self.labs.keys()))


class Location():
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity= capacity
        self.available = True


student_list = []
course_list= []
location_list = []

with open("vakken.csv") as c:
    next(c)
    for line in c:

        split_data = line.split(',')
        course_name = split_data[0]
        lectures_n = split_data[1]
        tutorial_n = split_data[2]
        tutorial_cap = split_data[3]
        labs_n = split_data[4]
        labs_cap = split_data[5]
        e_students = split_data[6]

        course = Course(course_name, lectures_n, tutorial_n, tutorial_cap, labs_n, labs_cap, e_students)
        course_list.append(course)

with open("studenten_en_vakken.csv") as sv:
    for line in sv:
        split_data = line.split(',')
        student_id = split_data[2]
        courses = [split_data[3],split_data[4],split_data[5],split_data[6],split_data[7]]

        student = Student(student_id, courses)
        student_list.append(student)

with open("zalen.csv") as z:
    for line in z:
        split_data = line.split(',')
        room_id = split_data[0]
        capacity = split_data[1]

        location = Location(room_id, capacity)

        location_list.append(location)


course_list[4].add_students_tut(student_list)
course_list[4].add_students_lab(student_list)
