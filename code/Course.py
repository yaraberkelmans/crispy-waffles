from .loading_data import Load_init_lists

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
