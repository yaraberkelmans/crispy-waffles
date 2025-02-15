import csv
import os
from .timeslot import Timeslot
from .course import Course, Tutorial, Lab, Lecture
import random
from .student import Student
from .location import Location
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
        self.conflict_students = []

    def create_timetable(self):
        """
        This method initializes the timetable by creating a Timeslot instance for each combination of day and time 
        and puts each Timeslot in an empty dictionary. 
        """
        for day in self.days:
            for time in self.times:
                self.timetable[Timeslot(day, time)] = {}
    

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
        This method creates and names activities (lectures, tutorials, labs) for each 
        course based on the activities count, and adds these activities to each respective 
        course's activities list and the timetable activity list. 
        """
        # loop over each courses' activities
        for course, activities_count_dict in self.activities_per_course.items():
            for activity_type, activity_amount in activities_count_dict.items():
                for i in range(activity_amount):

                    # make names for each activity based on their activity type
                    activity_name = f'{activity_type} {i+1}'

                    # make an instance of each activity
                    if activity_type == 'Tutorial':

                        # spread students evenly across each group
                        initial_capacity = len(course.student_list) / activity_amount
                        activity = Tutorial(course, course.tutorial_cap, initial_capacity, activity_name)
                    
                    elif activity_type == 'Lab':
                        initial_capacity = len(course.student_list) / activity_amount
                        activity = Lab(course, course.lab_cap, initial_capacity, activity_name)
                    
                    else:
                        activity = Lecture(course, activity_name)
                    
                
                    course.activities[activity_type].append(activity)
                    self.activity_list.append(activity)
     

    def add_student_to_activity(self, student, activity): # still not a scheduled activity
        """
        This method adds a student to an activity of a course the student follows, if the
        activity is not full and then updates the activity student list and the students'
        personal activities.
        """
        # check if student is not already in activity and student will fit in activity
        if student not in activity.student_list and student in activity.course.student_list and (len(activity.student_list) + 1) <= activity.capacity :
            activity.student_list.append(student)
            student.pers_activities[activity.course].append(activity)
            if activity.timeslot:
                student.fill_pers_timetable(activity)


    def add_actual_students_to_courses(self):
        """
        This method loops over each course and each student in the full student list and 
        then adds the student to the course if it attends the course. It then updates the
        courses' student list and the students personal activities.
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
            if activity.timeslot:
                student.pers_timetable[activity.timeslot.day].remove(activity.timeslot.time)
    
    def swap_student_activity(self, student, activity_out, activity_in):
        """
        This method swaps a students from one activity to another. 
        """
        if len(activity_in.student_list) < activity_in.capacity:
            self.remove_student_from_activity(student, activity_out)
            self.add_student_to_activity(student, activity_in)
            

    def switch_students(self, student_1, student_2, activity_1, activity_2):
        """
        This method switches two students from the same course between two activities if
        they are not in the same activity.
        """
        if student_1 in activity_2.course.student_list and student_2 not in activity_1.student_list:
            self.remove_student_from_activity(student_1, activity_1)
            self.remove_student_from_activity(student_2, activity_2)
            self.add_student_to_activity(student_1, activity_2)
            self.add_student_to_activity(student_2, activity_1)
        
    
    def remove_activity_from_timetable(self, activity):
        """
        This method removes an activity from the timetable by setting its timeslot and location to None. 
        """
        self.timetable[activity.timeslot][activity.location] = None
        for student in activity.student_list:
            student.remove_activity_pers_timetable(activity)


    def add_activity_to_timetable(self, activity, new_timeslot, new_location):
        """
        This method add an activity to a new timeslot and location in the timetable if the slot is still available. 
        """
        if self.timetable[new_timeslot][new_location] == None:
            self.timetable[new_timeslot][new_location] = activity
            activity.location = new_location
            activity.timeslot = new_timeslot
            for student in activity.student_list:
                student.fill_pers_timetable(activity)


    def switch_activity_in_timetable(self, activity, new_timeslot, new_location):
        """
        This method moves an activity to a new timeslot and location.  
        """

        self.remove_activity_from_timetable(activity)
        self.add_activity_to_timetable(activity, new_timeslot, new_location)
    

    def switch_activities_in_timetable(self, activity_1, activity_2):
        """
        This method moves an activity to a new timeslot and location. 
        """
        
        old_location_act_1 = activity_1.location
        old_location_act_2 = activity_2.location
        old_timeslot_act_1 = activity_1.timeslot
        old_timeslot_act_2 = activity_2.timeslot

        self.remove_activity_from_timetable(activity_1)
        self.remove_activity_from_timetable(activity_2)
        
        self.add_activity_to_timetable(activity_1, old_timeslot_act_2, old_location_act_2)
        self.add_activity_to_timetable(activity_2, old_timeslot_act_1, old_location_act_1)


    def find_empty_locations(self):
        """
        This method loops over all timeslot and location pairs and finds adds all pairs 
        not containing an activity to a empty locations list  
        """
        self.empty_locations = defaultdict(list)
        for timeslot in self.timetable.keys():
            for location in self.timetable[timeslot]:
                if self.timetable[timeslot][location] == None:
                    self.empty_locations[timeslot].append(location)


    def add_new_activity_to_course(self, course, activity_type):
        """
        This method adds a new activity of a certain activity_type to the timetable and course. 
        """
         # make names for each activity based on their activity type where i is the number for the activity
        i = len(course.activities[activity_type]) + 1
        activity_name = f'{activity_type} {i}'

        # make an instance of each activity
        if activity_type == 'Tutorial':
            initial_capacity = course.tutorial_cap
            activity = Tutorial(course, course.tutorial_cap, initial_capacity, activity_name)

        elif activity_type == 'Lab':
            initial_capacity = course.lab_cap
            activity = Lab(course, course.lab_cap, initial_capacity, activity_name)
          
        if activity:
            course.activities[activity_type].append(activity)
            self.activity_list.append(activity)  
        else:
            print(f'activity type {activity_type} not recognized')    
            return 

        return activity  

       
    def generate_initial_timetable(self):
        """
        This method generates and creates the initial timetable. 
        """
        #  load all data and create instances   
        self.load_courses('data/vakken.csv')
        self.load_students('data/studenten_en_vakken.csv')
        self.load_locations('data/zalen.csv')

        self.add_actual_students_to_courses()

        # create expected numbers does not add activity
        self.get_activities_count() 

        # add activity to course.activity
        self.name_activities() 

         # make empty .self attr
        self.create_timetable()

        # turn empty into None
        self.initialize_locations() 

