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
        self.classes = []

        # # only create a dictionary if there are tutorials or labs for this course
        # if int(self.tutorial_n) >= 1:
        #     self.tutorials = {}
        # if int(self.lab_n) >= 1:
        #     self.labs = {}

    def add_students_tut(self, student_list):
        """This method adds a certain list of students to seperate tutorial groups, based on the tutorials_cap per tutorial group. The tutorials are in a dictionary with the
        tutorial # as key and a list of students as values."""
        for x in range(1,self.expected_tut_n+1):
            stud_per_tut = len(student_list)/ self.expected_tut_n
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
                self.student_list.append(student.student_id)

    def add_individual_student(self, student):
        """This method adds an individual student to the student list of the course."""
        if student not in self.student_list: 
            self.student_list.append(student)
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
            
    # def __str__(self):
    #     return f"Course Name: {self.course_name}, Lectures: {self.lectures_n}, Tutorials: {self.tutorial_n}, Students: {self.student_list}, Labs: {self.lab_n}, Expected Students: {self.e_students}, All Students: {self.all_student_list}"

    def __repr__(self) -> str:
        return f"{self.course_name}"

class Tutorial(Course):
    def __init__(self, course_name, tutorial_cap, name):
        super().__init__(course_name, tutorial_cap=tutorial_cap)
        self.capacity = tutorial_cap 
        self.student_list = []
        self.name = name
        
    
    def __repr__(self) -> str:
        return f"{self.course_name} {self.name}"

class Lab(Course):
    def __init__(self, course_name, lab_cap, name):
        super().__init__(course_name, lab_cap=lab_cap)
        self.capacity = lab_cap
        self.student_list = []
        self.name = name
        
    
    def __repr__(self) -> str:
        return f"{self.course_name} {self.name}"

class Lecture(Course):
    def __init__(self, course_name, e_students, name):
        #print('Lecture init:',e_students, course_name)
        super().__init__(course_name, e_students=e_students)
        self.capacity = e_students
        self.student_list = []
        self.name = name
        
    
    def __repr__(self) -> str:
        return f"{self.course_name} {self.name}"