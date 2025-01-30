import random
import copy
from .malus import *

class Randomize():
    """
    This class represents the randomization algorithm, which is also the baseline
    algorithm of this software. The randomization algorithm first randomly assigns 
    students to activity groups, such as tutorials and labs and then randomly assigns
    activities to timeslot and location pairs.
    """
    def __init__(self, timetable):
        self.timetable = copy.deepcopy(timetable)

    def run(self):
        """
        This method creates a new random timetable by random assigning courses, activities and students to timeslots and rooms.
        """
        self.random_student_activity_assignment()
        self.random_course_assignment()

        return self.timetable


    def random_course_assignment(self):
        """
        This method randomly assigns activities to timeslots and rooms in the timetable until all activities are assigned.
        """
        new_activities_list = copy.copy(self.timetable.activity_list)
        activity_count = len(new_activities_list)

        new_timetable_dict = self.timetable.timetable
        activities_added = 0

        # while we still have activities to assign to timeslots, continue the loop
        while activities_added < activity_count:

            # randomly choose a timeslot and room for a random activity
            random_timeslot = random.choice(list(new_timetable_dict.keys()))
            random_room = random.choice(list(new_timetable_dict[random_timeslot]))
            random_activity = random.choice(list(new_activities_list))
            
            # only if the timeslot and room are still empty we assign the activity
            if new_timetable_dict[random_timeslot][random_room] == None:
                new_timetable_dict[random_timeslot][random_room] = random_activity
                random_activity.timeslot = random_timeslot
                random_activity.location = random_room
                new_activities_list.remove(random_activity)
            
                for student in random_activity.student_list:
                    student.fill_pers_timetable(random_activity)
                
                # keep track of the added activities
                activities_added += 1

        
    def random_student_course_assignment(self, timetable):
        """
        This method randomly assigns students to courses 
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


    def random_student_activity_assignment(self):
        """
        This method randomly assigns students to activities within their courses,
        taking the capacity constraints of the activity into account. 
        """
        for course in self.timetable.courses:
            
            for activity_type in course.activities.keys():

                # loop over all the activities except the last one
                for activity in course.activities[activity_type][:-1]:

                    # if there is still room in the activity and the student is valid for placement add student the activity
                    while len(activity.student_list) < activity.initial_capacity:
                        valid_students = [st for st in course.student_list if st not in activity.student_list 
                                        and st.check_validity(activity)]
                        
                        # no more valid students break to avoid infinite loop
                        if not valid_students:
                            break

                        random_student = random.choice(valid_students)
                        self.timetable.add_student_to_activity(random_student, activity)

                # place remaining students in the last activity
                last_activity = course.activities[activity_type][-1]
                valid_students = [st for st in course.student_list if st not in last_activity.student_list 
                                and st.check_validity(last_activity)]
                
                for student in valid_students:
                    self.timetable.add_student_to_activity(student, last_activity)
                















