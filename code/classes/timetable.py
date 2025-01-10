from loading_data import Load_init_lists
import csv
import os
from Timeslot import Timeslot
from Course import Course

class Timetable():
    def __init__(self):
        """
        Inputs days and times are lists and for every combination, 
        a timeslot instance is created to be used as the key for the dictionary, 
        the value is an empty diictionary.
        """
        self.days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        self.times = ['9-11', '11-13', '13-15', '15-17']
        self.course_classes = {}
        self.classes_list = []
    def create_timetable(self):
        for day in self.days:
            for time in self.times:
                self.timetable[Timeslot(day, time)] = {}
        
    def fill_locations(self):
        pass

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
            self.course_classes[course.course_name] = {'Lectures': course.lectures_n, 'Tutorials': course.expected_tut_n, 'Labs': course.expected_lab_n}

    def name_classes(self):
        self.classes_list = []
        for course_name, classes_count_dict in self.course_classes.items():
            for class_type, class_amount in classes_count_dict.items():
                for i in range(class_amount):
                    class_name = course_name + ' ' + class_type + ' ' + str(i+1)
                    self.classes_list.append(class_name)
        

print(os.getcwd())
timetable = Timetable()
timetable.load_courses('data/vakken.csv')
timetable.get_classes_count()
timetable.name_classes()
print(timetable.courses[1].course_name)
print(timetable.classes_list)

