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
        

print(os.getcwd())
timetable = Timetable()
timetable.load_courses('data/vakken.csv')
timetable.get_classes_count()
print(timetable.courses[1].course_name)
print(timetable.course_classes)
