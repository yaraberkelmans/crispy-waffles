import csv
import os
from .Timeslot import Timeslot
from .Course import Course, Tutorial, Lab, Lecture
import random
from .Student import Student
from .Location import Location

from typing import Dict

class Timetable():
    def __init__(self):
        """
        Inputs days and times are lists and for every combination, 
        a timeslot instance is created to be used as the key for the dictionary, 
        the value is an empty diictionary.
        """
        self.days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        self.times = ['9-11', '11-13', '13-15', '15-17']

        self.locations = []
        self.activities_per_course = {}
        self.activity_list = []
        self.timetable: Dict[Timeslot: Dict[Location: "activity"]] = {}
        self.full_student_list = []
        self.courses = []

    def create_timetable(self):
        for day in self.days:
            for time in self.times:
                self.timetable[Timeslot(day, time)] = {}
    
    # TODO: incorporate this function in create timetable or init func in a handy way to simplify (defaultdict maybe)
    def initialize_locations(self):
        for timeslot in self.timetable.keys():
            for location in self.locations:
                self.timetable[timeslot][location] = None

    #TODO: een universele functie maken van alle load functies
    def load_courses(self, input_file):
        with open(input_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                course = Course(row['Vak'], row['#Hoorcolleges'], 
                                row['#Werkcolleges'], row['Max. stud. Werkcollege'],
                                row['#Practica'], row['Max. stud. Practicum'],
                                row['Verwacht'])
                self.courses.append(course)
    
    def load_students(self, input_file):
        with open(input_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                student = Student(row['Achternaam'], row['Voornaam'], 
                                row['Stud.Nr.'])
                self.full_student_list.append(student)
    
    def load_locations(self, input_file):
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                location = Location(row['Zaalnummer'], row['Max. capaciteit'])
                self.locations.append(location)

    def get_activities_count(self):
        for course in self.courses:
            course.count_groups()
            self.activities_per_course[course] = {'Lecture': course.lectures_n,
                                                           'Tutorial': course.expected_tut_n,
                                                           'Lab': course.expected_lab_n}

    def name_activities(self):  
        # TODO: Make it list comprehension instead of loop
        for course, activities_count_dict in self.activities_per_course.items():
            for activity_type, activity_amount in activities_count_dict.items():
                for i in range(activity_amount):
                    activity_name = f'{activity_type} {i+1}'
                    if activity_type == 'Tutorial':
                        activity = Tutorial(course, course.tutorial_cap, activity_name)
                    elif activity_type == 'Lab':
                        activity = Lab(course, course.lab_cap, activity_name)
                    else:
                        activity = Lecture(course, course.e_students, activity_name)
                    
                    course.activities.append(activity)
                    self.activity_list.append(activity)
                    # print(f'activity {activity_name} added!')

    def add_student_to_activity(self, student, activity): # still not a scheduled activity
        """
        Currently only updates timetable.course_list!
        """
        if activity not in self.activity_list:
            print(f'activity {activity} does not exist.')
        
        if student not in activity.student_list and student in activity.course.student_list:
            activity.student_list.append(student)
            student.pers_timetable[activity.course].append(activity)
        else:
            print(f'Student {student.name} already in activity {activity}.')

    
        

print(os.getcwd())
timetable = Timetable()
timetable.load_courses('data/vakken.csv')
timetable.get_activities_count()
timetable.name_activities()
timetable.create_timetable()
timetable.initialize_locations()
#print(timetable.courses[1].course_name)
'''
for timeslot in timetable.timetable.keys():
    print(timeslot.name)
'''
#print(timetable.timetable)

