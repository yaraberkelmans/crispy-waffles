from .Course import Course, Tutorial, Lab, Lecture
from collections import defaultdict

class Student():
    """
    This class represents a student with a name, ID and a list of courses that the student follows.
    """
    def __init__(self, last_name, first_name, student_id, courses=[]):
        self.student_id = student_id
        self.courses = set(courses)
        self.activities = []
        self.is_valid = True
        self.placed = False    
        self.first_name = first_name
        self.last_name = last_name
        self.name = f'{first_name} {last_name}'
        self.conflict_points = 0

        # key is course, value is a list of activities
        self.pers_activities = defaultdict(list)

        # key is day, value is list of timeslots that are being used
        self.pers_timetable = defaultdict(list)
    
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.student_id}"
    
    def check_validity(self, activity):  
        """
        This method checks for a student if this student has already been added to a tutorial or lab for this course.
        If so, it returns False otherwise it returns True.
        """
        for value in self.pers_activities[activity.course]:
            if type(activity) == Tutorial or type(activity) == Lab:
                if isinstance(activity, type(value)):
                    return False
        return True
    
    def fill_pers_timetable(self, activity):
        self.pers_timetable[activity.timeslot.day].append(activity.timeslot.time)

    def update_pers_timetable(self, activity):
        self.pers_timetable = defaultdict(list)
        for activity in self.activities:
            self.pers_timetable[activity.timeslot.day].append(activity.timeslot.time)