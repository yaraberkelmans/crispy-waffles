import csv
import os
from .Timeslot import Timeslot
from .Course import Course
import random

class Timetable():
    def __init__(self):
        """
        Inputs days and times are lists and for every combination, 
        a timeslot instance is created to be used as the key for the dictionary, 
        the value is an empty diictionary.
        """
        self.days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        self.times = ['9-11', '11-13', '13-15', '15-17']
        self.locations = ['A1.04', 'A1.06', 'A1.08', 'A1.10','B0.201', 'C0.110', 'C1.112']
        self.classes_per_course = {}
        self.classes_list = {}
        self.timetable = {}
    
    def create_timetable(self):
        for day in self.days:
            for time in self.times:
                self.timetable[Timeslot(day, time).name] = {}
    
    # TODO: incorporate this function in create timetable or init func in a handy way to simplify (defaultdict maybe)
    def initialize_locations(self):
        for timeslot in self.timetable.keys():
            for location in self.locations:
                self.timetable[timeslot][location] = None

    def load_courses(self, input_file):
        self.courses = []
        with open(input_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                course = Course(row['Vak'], row['#Hoorcolleges'], 
                                row['#Werkcolleges'], row['Max. stud. Werkcollege'],
                                row['#Practica'], row['Max. stud. Practicum'],
                                row['Verwacht'])
                self.courses.append(course)

    def get_classes_count(self):
        for course in self.courses:
            course.count_groups()
            self.classes_per_course[course.course_name] = {'Lecture': course.lectures_n,
                                                           'Tutorial': course.expected_tut_n,
                                                           'Lab': course.expected_lab_n}

    def name_classes(self):  
        # TODO: Make it list comprehension instead of loop
        for course_name, classes_count_dict in self.course_classes.items():
            for class_type, class_amount in classes_count_dict.items():
                for i in range(class_amount):
                    class_name = f'{course_name} {class_type} {i+1}'
                    self.classes_list[class_name] = []

    def add_student_to_class(self, student, class_name):
        if class_name not in self.classes_list.keys():
            print(f'Class {class_name} does not exist.')
            return
        
        if student not in self.classes_list[class_name]:
            self.classes_list[class_name].append(student)
        else:
            print(f'Student {student.name} already in Class {class_name}.')
        

print(os.getcwd())
timetable = Timetable()
timetable.load_courses('data/vakken.csv')
timetable.get_classes_count()
timetable.name_classes()
timetable.create_timetable()
timetable.initialize_locations()
#print(timetable.courses[1].course_name)
'''
for timeslot in timetable.timetable.keys():
    print(timeslot.name)
'''
#print(timetable.timetable)

