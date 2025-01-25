import csv
from collections import defaultdict
class Course():
    """
    This class represents a course with lectures, tutorials, labs, and students.
    """
    def __init__(self, course_name, lectures_n=0, tutorial_n=0, tutorial_cap=0, lab_n=0, lab_cap=0, e_students=0):
        self.course_name = course_name
        self.lectures_n = int(lectures_n)
        self.tutorial_n = int(tutorial_n)
        self.student_list = []
        self.lab_n = int(lab_n)
        self.e_students = int(e_students)
        self.all_student_list = []
        self.actual_lab_n = 0
        self.actual_tut_n = 0
        if tutorial_cap:
            self.tutorial_cap = int(tutorial_cap)
        if lab_cap:
            self.lab_cap = int(lab_cap)
        self.activities = defaultdict(list)


    def add_students_tut(self, student_list, capacity):
        """
        This method adds a certain list of students to seperate tutorial groups, based on the tutorials_cap per tutorial group. The tutorials are in a dictionary with the
        tutorial number as key and a list of students as values.
        """
        for x in range(1,len(self.student_list)+1):
            stud_per_tut = len(self.student_list)/ self.expected_tut_n
            self.tutorials[x] = student_list[round(((x-1) * stud_per_tut)):round((x *stud_per_tut))]
        print(len(self.tutorials.keys()))

    def add_students_lab(self, student_list):
        """
        This method adds a certain list of students to seperate lab groups, based on the lab_cap per lab group. The labs are in a dictionary with the
        lab number as key and a list of students as values.
        """
        for x in range(1,self.expected_lab_n+1):
            stud_per_lab = len(student_list)/ self.expected_lab_n
            self.labs[x] = student_list[round(((x-1) * stud_per_lab)):round((x *stud_per_lab))]
        print(len(self.labs.keys()))

    def add_actual_students_to_courses(self):
        """
        This method adds a student to the course, based on the courses list in a Student instance.
        """
        for student in self.all_student_list:
            if self.course_name in student.courses:
                self.student_list.append(student)

    def add_individual_student(self, student):
        """
        This method adds an individual student to the student list of the course.
        """
        if student not in self.student_list and self not in student.pers_activities: 
            self.student_list.append(student)

            # pas op! maakt elke keer lege lijst met activities aan, swappen met werkgroep
            student.pers_activities[self] = []
            
        else:
            print('Student already in course')
    
    def remove_student(self, student):
        """
        This method removes an individual student from the students list of the course.
        """
        pass

    def count_groups(self):
        """
        This method calculates the amount of tutorial and lab groups needed to fit all the expected students.
        """
        if self.tutorial_n > 0:
            self.activities['Tutorial'] = []
            self.expected_tut_n = len(self.student_list) // self.tutorial_cap
            if len(self.student_list) % self.tutorial_cap > 0:
                self.expected_tut_n += 1
                
        else:
            self.expected_tut_n = 0

        if self.lab_n > 0:
            self.activities['Lab'] = []
            self.expected_lab_n = len(self.student_list) // self.lab_cap 
            if len(self.student_list) % self.lab_cap > 0:
                self.expected_lab_n += 1
                
        else:
            self.expected_lab_n = 0
            
    def __repr__(self) -> str:
        return f"{self.course_name}"

class Tutorial():
    """
    This class represents a tutorial group within a course.
    """
    def __init__(self, course, tutorial_cap, initial_capacity, name):
        self.course = course  
        self.capacity = tutorial_cap
        self.student_list = []
        self.name = name
        self.timeslot = None
        self.location = None
        self.over_capacity = False
        self.initial_capacity = initial_capacity
        self.activity_type = 'Tutorial'

    def __repr__(self):
        return f"{self.course} {self.name}"


class Lab():
    """
    This class represents a lab group within a course.
    """
    def __init__(self, course, lab_cap, initial_capacity, name):
        self.course = course  
        self.capacity = lab_cap
        self.student_list = []
        self.over_capacity = 0
        self.name = name
        self.timeslot = None
        self.location = None
        self.initial_capacity = initial_capacity
        self.activity_type = 'Lab'

    def __repr__(self):
        return f"{self.course} {self.name}"


class Lecture():
    """
    This class represents a lecture group within a course.
    """
    def __init__(self, course, name):
        self.course = course  
        self.capacity = len(course.student_list)
        self.student_list = []
        self.name = name
        self.timeslot = None
        self.location = None
        self.over_capacity = 0
        self.activity_type = 'Lecture'

        # to avoid conflict in random student activity assignment
        self.initial_capacity = len(course.student_list)

    def __repr__(self):
        return f"{self.course} {self.name}"