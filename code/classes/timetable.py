import csv
import os
from .Timeslot import Timeslot
from .Course import Course, Tutorial, Lab, Lecture
import random
from .Student import Student
from .Location import Location
from collections import defaultdict

from typing import Dict

class Timetable():
    """
    This class represents a timetable, consisting of courses, students, locations and activities.
    """
    def __init__(self):
        """
        Inputs days and times are lists and for every combination, 
        a timeslot instance is created to be used as the key for the dictionary, 
        the value is an empty diictionary.
        """
        self.days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        self.times = ['9-11', '11-13', '13-15', '15-17', '17-19']

        self.locations = []
        self.activities_per_course = {}
        self.activity_list = []
        self.timetable: Dict[Timeslot: Dict[Location: "activity"]] = {}
        self.full_student_list = []
        self.courses = []
        

    def create_timetable(self):
        """
        This method initializes the timetable by creating a Timeslot instance for each combination of day and time 
        and maps each Timeslot to an empty dictionary. 
        """
        for day in self.days:
            for time in self.times:
                self.timetable[Timeslot(day, time)] = {}
    
    # TODO: incorporate this function in create timetable or init func in a handy way to simplify (defaultdict maybe)
    def initialize_locations(self):
        """
        This method fills the timetable with locations for each timeslot and initializes them with None.
        """
        for timeslot in self.timetable.keys():
            for location in self.locations:
                if timeslot.time == '17-19' and location.room_id != 'C0.110':
                    continue
                else:
                    self.timetable[timeslot][location] = None

    #TODO: een universele functie maken van alle load functies
    def load_courses(self, input_file):
        """
        This method loads courses from a CSV file and adds them to the courses list. 
        """
        with open(input_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                course = Course(row['Vak'], row['#Hoorcolleges'], 
                                row['#Werkcolleges'], row['Max. stud. Werkcollege'],
                                row['#Practica'], row['Max. stud. Practicum'],
                                row['Verwacht'])
                self.courses.append(course)
    
    def load_students(self, input_file):
        """
        This method loads students from a CSV file and adds them to the full student list. 
        """
        with open(input_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:

                student = Student(row['Achternaam'], row['Voornaam'], 
                                row['Stud.Nr.'],[row['Vak1'], row['Vak2'], row['Vak3'], row['Vak4'], row['Vak5']])
                self.full_student_list.append(student)
    
    def load_locations(self, input_file):
        """
        This method loads locations from a CSV file and adds them to the locations list. 
        """
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                location = Location(row['Zaalnummer'], row['Max. capaciteit'])
                self.locations.append(location)

    def get_activities_count(self):
        """
        This method calculates and stores the number of lectures, tutorials and labs for each course 
        and updates the dictionary holding activities per course. 
        """
        for course in self.courses:
            course.count_groups()
            self.activities_per_course[course] = {'Lecture': course.lectures_n,
                                                           'Tutorial': course.expected_tut_n,
                                                           'Lab': course.expected_lab_n}

    def name_activities(self):  
        """
        This method creates and names activities (lectures, tutorials, labs) for each course based on the activities count, 
        and updates the course's activities list and the overall activity list. 
        """
        # TODO: Make it list comprehension instead of loop
        for course, activities_count_dict in self.activities_per_course.items():
            for activity_type, activity_amount in activities_count_dict.items():
                for i in range(activity_amount):
                    activity_name = f'{activity_type} {i+1}'
                    if activity_type == 'Tutorial':
                        initial_capacity = len(course.student_list) / activity_amount
                        activity = Tutorial(course, course.tutorial_cap, initial_capacity, activity_name)
                    elif activity_type == 'Lab':
                        initial_capacity = len(course.student_list) / activity_amount
                        activity = Lab(course, course.lab_cap, initial_capacity, activity_name)
                    else:
                        activity = Lecture(course, activity_name)
                    
                    course.activities[activity_type].append(activity)
                    self.activity_list.append(activity)
                    # print(f'activity {activity_name} added!')
        # print(f'Timetable activities list {self.activity_list}')
        # print(f'length: {len(self.activity_list)}')

    def add_student_to_activity(self, student, activity): # still not a scheduled activity
        """
        This method adds a student to an activity of a course the student follows, if the activity is not full.
        Currently only updates timetable.course_list!
        """
        #if activity not in self.activity_list:
        #    print(f'activity {activity} does not exist.')
        
        if student not in activity.student_list and student in activity.course.student_list and (len(activity.student_list) + 1) <= activity.capacity :
            activity.student_list.append(student)
            student.pers_activities[activity.course].append(activity)
        # else:
        #    print(f'Student {student.name} already in activity {activity}.')


    def add_actual_students_to_courses(self):
        """
        This method adds a student to the course, based on the courses list in a Student instance.
        """
        for course in self.courses:
            for student in self.full_student_list:
                if course.course_name in student.courses:
                    course.student_list.append(student)
                    student.pers_activities[course] = []

    def remove_student_from_activity(self, student, activity):
        """
        This method removes a student from an activity and updates their personal timetable.
        """
        if student in activity.student_list:
            activity.student_list.remove(student)
            student.pers_activities[activity.course].remove(activity)
            
    # probably unnecessary
    def swap_student_activity(self, student, activity_out, activity_in):
        """
        This method swaps a students from one activity to another. 
        """
        if len(activity_in.student_list) < activity_in.capacity:
            self.remove_student_from_activity(student, activity_out)
            self.add_student_to_activity(student, activity_in)
        # else:
        #     print(f'Tried to add student {student}, to filled activity {activity_in}')

    def switch_students(self, student_1, student_2, activity_1, activity_2):
        """
        This method switches two students between two activities.
        """
        # self.swap_student_activity(student_1, activity_1, activity_2)
        # self.swap_student_activity(student_2, activity_2, activity_1)
        if student_1 in activity_2.course.student_list and student_2 not in activity_1.student_list:
            self.remove_student_from_activity(student_1, activity_1)
            self.remove_student_from_activity(student_2, activity_2)
            self.add_student_to_activity(student_1, activity_2)
            self.add_student_to_activity(student_2, activity_1)
            student_1.update_pers_timetable(activity_2)
            student_2.update_pers_timetable(activity_1)
    
    def remove_activity_from_timetable(self, activity):
        self.timetable[activity.timeslot][activity.location] = None

    def add_activity_to_timetable(self, activity, new_timeslot, new_location):
        if self.timetable[new_timeslot][new_location] == None:
            self.timetable[new_timeslot][new_location] = activity
            activity.location = new_location
            activity.timeslot = new_timeslot

    # probably unnecessary
    def switch_activity_in_timetable(self, activity, new_timeslot, new_location):
        self.remove_activity_from_timetable(activity)
        self.add_activity_to_timetable(activity, new_timeslot, new_location)
    
    def switch_activities_in_timetable(self, activity_1, activity_2):
        old_location_act_1 = activity_1.location
        old_location_act_2 = activity_2.location
        old_timeslot_act_1 = activity_1.timeslot
        old_timeslot_act_2 = activity_2.timeslot

        self.remove_activity_from_timetable(activity_1)
        self.remove_activity_from_timetable(activity_2)
        self.add_activity_to_timetable(activity_1, old_timeslot_act_2, old_location_act_2)
        self.add_activity_to_timetable(activity_2, old_timeslot_act_1, old_location_act_1)

    def find_empty_locations(self):
        self.empty_locations = defaultdict(list)
        for timeslot in self.timetable.keys():
            for location in self.timetable[timeslot]:
                if self.timetable[timeslot][location] == None:
                    self.empty_locations[timeslot].append(location)


    def generate_initial_timetable(self):
        self.load_courses('data/vakken.csv') # adds course obj to self
        self.load_students('data/studenten_en_vakken.csv')
        self.load_locations('data/zalen.csv')
        self.add_actual_students_to_courses()
        self.get_activities_count() # creates expected numbers, does not add activity
        self.name_activities() # adds activity to course.activity
        self.create_timetable() # makes empty .self attr
        self.initialize_locations() # turns empty into None



        

#print(os.getcwd())
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

