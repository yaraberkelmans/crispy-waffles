from loading_data import Load_init_lists
import csv

class Course():
    def __init__(self, course_name, lectures_n, tutorial_n, tutorial_cap=0, labs_n=0, labs_cap=0, e_students=0):
        self.course_name = course_name
        self.lectures_n = int(lectures_n)
        self.tutorial_n = int(tutorial_n)
        
        self.labs_n = int(labs_n)
        
        self.e_students = int(e_students)
        self.tot_student_list = []
        if tutorial_cap:
            self.tutorial_cap = int(tutorial_cap)
        if labs_cap:
            self.labs_cap = int(labs_cap)
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
            self.expected_tut_n = self.e_students // self.tutorial_cap
            if self.e_students % self.tutorial_cap > 0:
                self.expected_tut_n += 1
        else:
            self.expected_tut_n = 0

        if self.labs_n > 0:
            self.expected_lab_n = self.e_students // self.labs_cap 
            if self.e_students % self.labs_cap > 0:
                self.expected_lab_n += 1
        else:
            self.expected_lab_n = 0

