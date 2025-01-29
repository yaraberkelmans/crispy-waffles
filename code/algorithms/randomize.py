import random
import copy
from .malus import *

class Randomize():
    def __init__(self, timetable):
        self.timetable = timetable

    def randomize(timetable):
        """
        This function creates a new random timetable by random assigning courses, activities and students to timeslots and rooms.
        """
        new_timetable = copy.deepcopy(timetable)
        
        randomized_student_courses_activities = random_student_activity_assignment(new_timetable)
        randomized_timetable = random_course_assignment(randomized_student_courses_activities)

        return randomized_timetable


    def random_course_assignment(timetable):
        """
        This function randomly assigns activities to timeslots and rooms in the timetable until all activities are assigned.
        """
        new_timetable = copy.copy(timetable)
        new_activities_list = copy.copy(new_timetable.activity_list)
        activity_count = len(new_activities_list)

        new_timetable_dict = new_timetable.timetable
        activities_added = 0

        while activities_added < activity_count:
            random_timeslot = random.choice(list(new_timetable_dict.keys()))
            random_room = random.choice(list(new_timetable_dict[random_timeslot]))
            random_activity = random.choice(list(new_activities_list))
            
            if new_timetable_dict[random_timeslot][random_room] is None:
                new_timetable_dict[random_timeslot][random_room] = random_activity
                random_activity.timeslot = random_timeslot
                random_activity.location = random_room
                new_activities_list.remove(random_activity)
            
                for student in random_activity.student_list:
                    student.fill_pers_timetable(random_activity)
                activities_added += 1

        return new_timetable


    def random_student_course_assignment(timetable):
        """
        This function randomly assigns students to courses 
        until the expected number of students per course is met.
        """
        new_timetable = timetable

        for course in new_timetable.courses:
            while len(course.student_list) < course.e_students:
                random_student = random.choice(new_timetable.full_student_list)
                
                if random_student in course.student_list:
                    continue

                course.add_individual_student(random_student)
                
        return new_timetable


    def random_student_activity_assignment(timetable):
        """
        This function randomly assigns students to activities within their courses,
        taking the capacity constraints of the activity into account. 
        """
        new_timetable = timetable

        for course in new_timetable.courses: # not your timetable
            
            for activity_type in course.activities.keys():

                for activity in course.activities[activity_type][:-1]:

                    while len(activity.student_list) < activity.initial_capacity:
                        valid_students = [st for st in course.student_list if st not in activity.student_list 
                                        and st.check_validity(activity)]
                        
                        # no more valid students break to avoid infinite loop
                        if not valid_students:
                            break

                        random_student = random.choice(valid_students)
                        new_timetable.add_student_to_activity(random_student, activity)

                # place remaining students in the last activity
                last_activity = course.activities[activity_type][-1]
                valid_students = [st for st in course.student_list if st not in last_activity.student_list 
                                and st.check_validity(last_activity)]
                
                for student in valid_students:
                    new_timetable.add_student_to_activity(student, last_activity)
                
        return new_timetable















