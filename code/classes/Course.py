from loading_data import Load_init_lists
import csv

class Course():
    def __init__(self, course_name, lectures_n, tutorial_n, tutorial_cap, labs_n, labs_cap, e_students):
        self.course_name = course_name
        self.lectures_n = lectures_n
        self.tutorial_n = tutorial_n
        self.tutorial_cap = tutorial_cap
        self.labs_n = labs_n
        self.labs_cap = labs_cap
        self.e_students = e_students
        self.tot_student_list = []
        if int(self.tutorial_n) >= 1:
            self.tutorials = {}
        if int(self.labs_n) >= 1:
            self.labs = {}

    def add_students_tut(self, student_list):
        """This method adds a certain list of students to seperate tutorial groups, based on the tutorials_cap per tutorial group. The tutorials are in a dictionary with the
        tutorial # as key and a list of students as values"""
        for x in range(1,self.expected_tut_n+1):
            stud_per_tut = len(student_list)/ self.expected_tut_n
            self.tutorials[x] = student_list[round(((x-1) * stud_per_tut)):round((x *stud_per_tut))]
        print(len(self.tutorials.keys()))

    def add_students_lab(self, student_list):
        """This method adds a certain list of students to seperate lab groups, based on the labs_cap per lab group. The labs are in a dictionary with the
        lab # as key and a list of students as values"""
        for x in range(1,self.expected_lab_n+1):
            stud_per_lab = len(student_list)/ self.expected_lab_n
            self.labs[x] = student_list[round(((x-1) * stud_per_lab)):round((x *stud_per_lab))]
        print(len(self.labs.keys()))

    def add_students(self):
        self.course_student_list = []
        for student in self.tot_student_list:
            if self.course_name in student.courses:
                self.course_student_list.append(student.student_id)

    def count_groups(self):
        if self.tutorial_n > 0:
            self.expected_tut_n = len(self.e_students) // int(self.tutorial_cap)
            if len(self.e_students) % int(self.tutorial_cap) > 0:
                self.expected_tut_n += 1
            
        if self.labs_n > 0:
            self.expected_lab_n = len(self.e_students) // int(self.labs_cap) 
            if len(self.e_students) % int(self.labs_cap) > 0:
                self.expected_lab_n += 1

class CourseLoader():
    def __init__(self, input_file):
        self.input_file = input_file

    def load_courses(self):
        self.courses = []
        with open(self.input_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
import os
gcw = os.path

course_loader = CourseLoader('../../data/vakken.csv')
course_loader.load_courses()