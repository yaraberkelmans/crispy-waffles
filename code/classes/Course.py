import csv

class Course():
    def __init__(self, course_name, lectures_n=0, tutorial_n=0, tutorial_cap=0, lab_n=0, lab_cap=0, e_students=0):
        self.course_name = course_name
        self.lectures_n = int(lectures_n)
        self.tutorial_n = int(tutorial_n)
        self.student_list = []
        self.lab_n = int(lab_n)
        self.e_students = int(e_students)
        self.all_student_list = []
        if tutorial_cap:
            self.tutorial_cap = int(tutorial_cap)
        if lab_cap:
            self.lab_cap = int(lab_cap)
        self.activities = []


    def add_students_tut(self, student_list, capacity):
        """This method adds a certain list of students to seperate tutorial groups, based on the tutorials_cap per tutorial group. The tutorials are in a dictionary with the
        tutorial # as key and a list of students as values."""
        for x in range(1,len(self.student_list)+1):
            stud_per_tut = len(self.student_list)/ self.expected_tut_n
            self.tutorials[x] = student_list[round(((x-1) * stud_per_tut)):round((x *stud_per_tut))]
        print(len(self.tutorials.keys()))

    def add_students_lab(self, student_list):
        """This method adds a certain list of students to seperate lab groups, based on the lab_cap per lab group. The labs are in a dictionary with the
        lab # as key and a list of students as values."""
        for x in range(1,self.expected_lab_n+1):
            stud_per_lab = len(student_list)/ self.expected_lab_n
            self.labs[x] = student_list[round(((x-1) * stud_per_lab)):round((x *stud_per_lab))]
        print(len(self.labs.keys()))

    def add_actual_students(self):
        """This method adds a student to the course, based on the courses list in a Student instance."""
        for student in self.all_student_list:
            if self.course_name in student.courses:
                self.student_list.append(student)

    def add_individual_student(self, student):
        """This method adds an individual student to the student list of the course."""
        if student not in self.student_list and self not in student.pers_timetable: 
            self.student_list.append(student)
            student.pers_timetable[self] = []
            
        else:
            print('Student already in course')
    
    def remove_student(self, student):
        pass

    def count_groups(self):
        """This method calculates the amount of tutorial and lab groups needed to fit all the expected students."""
        if self.tutorial_n > 0:
            self.expected_tut_n = self.e_students // self.tutorial_cap
            if self.e_students % self.tutorial_cap > 0:
                self.expected_tut_n += 1
        else:
            self.expected_tut_n = 0

        if self.lab_n > 0:
            self.expected_lab_n = self.e_students // self.lab_cap 
            if self.e_students % self.lab_cap > 0:
                self.expected_lab_n += 1
        else:
            self.expected_lab_n = 0
            
    def __repr__(self) -> str:
        return f"{self.course_name}"

class Tutorial():
    def __init__(self, course, tutorial_cap, name):
        self.course = course  
        self.capacity = tutorial_cap
        self.student_list = []
        self.name = name
        self.timeslot = None
        self.location = None

    def __repr__(self):
        return f"{self.course} {self.name}"


class Lab():
    def __init__(self, course, lab_cap, name):
        self.course = course  
        self.capacity = lab_cap
        self.student_list = []
        
        self.name = name
        self.timeslot = None
        self.location = None

    def __repr__(self):
        return f"{self.course} {self.name}"


class Lecture():
    def __init__(self, course, e_students, name):
        self.course = course  
        self.capacity = e_students
        self.student_list = course.student_list 
        self.name = name
        self.timeslot = None
        self.location = None

    def __repr__(self):
        return f"{self.course} {self.name}"