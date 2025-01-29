import copy
import random
from .malus import *

class Algorithm():
    def __init__(self, timetable):
        self.timetable = copy.deepcopy(timetable)   

    def random_students_swap(self):
        """
        This function randomly chooses a course, then chooses a random activity type
        either tutorial or lab and then chooses two different groups within this course
        and activity type to pick a student out of each of the groups and then switches them
        from group. 
        """
        random_course = self.pick_random_course()

        # avoid courses containing only lectures
        while list(random_course.activities.keys()) == ['Lecture']:
            random_course = self.pick_random_course()

        activity_type = random.choice(list(random_course.activities.keys()))

        # avoid lectures and other activities with less than 2 groups
        while activity_type == 'Lecture' or len(random_course.activities[activity_type]) < 2:
            activity_type = random.choice(list(random_course.activities.keys()))

        random_activity_1 = self.pick_activity_from_course(activity_type, random_course)
        random_activity_2 = self.pick_activity_from_course(activity_type, random_course)

        # avoids choosing same activity group
        while random_activity_1 == random_activity_2:
            random_activity_2 = self.pick_activity_from_course(activity_type, random_course)

        random_student_1 = random.choice(random_activity_1.student_list)
        random_student_2 = random.choice(random_activity_2.student_list)

        self.timetable.switch_students(random_student_1, random_student_2, random_activity_1, random_activity_2)

        return self.timetable


    def random_activities_swap(self):
        """
        This function chooses two random activities and then switches their timeslots
        and locations to switch them around in the self.timetable.
        """
        random_activity_1 = self.pick_random_activity()
        random_activity_2 = self.pick_random_activity()
        
        # if the same activities are chosen pick a new activity
        while random_activity_1 == random_activity_2:
            random_activity_2 = self.pick_random_activity()
        
        self.timetable.switch_activities_in_self.timetable(random_activity_1, random_activity_2)

        return self.timetable

    def random_activity_location_swap(self):
        """
        This function randomly chooses an activity to switch to a random empty
        location.
        """
        random_activity = self.pick_random_activity()

        # refresh empty location list
        self.timetable.find_empty_locations()

        # choose from empty locations
        random_timeslot = random.choice(list(self.timetable.empty_locations.keys()))
        random_location = random.choice(list(self.timetable.empty_locations[random_timeslot]))
        
        # choose random activity instead of new random empty location to avoid infinite loop if all location
        # capacities are smaller then length activity student list
        while random_location.capacity < len(random_activity.student_list):
            random_activity = self.pick_random_activity()
        
        self.timetable.switch_activity_in_self.timetable(random_activity, random_timeslot, random_location)

        return self.timetable


    def switch_conflict_student(self):
        """
        This function chooses a student out of all students that have conflicting activities. It
        tries to do this 20 times to prevent choosing a student that only has lectures as 
        conflicting activities (because each student following a course attends each lecture) or
        choosing a student for who all conflicting activity groups are full.
        """
        
        # make sure to stop after 20 attempts if all conflict students only have lectures 
        # or for every student every other group for conflict activity type is full
        for i in range(20):
            random_student = random.choice(self.timetable.conflict_students)

            random_timeslot = random.choice(list(random_student.conflict_activities.keys()))

            conflict_activity_list = random_student.conflict_activities[random_timeslot]
            random_activity = random.choice(conflict_activity_list)

            # go to next iteration of loop if chosen activity type is lecture
            if random_activity.activity_type == 'Lecture':
                continue

            random_course = random_activity.course
            activity_type = random_activity.activity_type

            # check if there are at least 2 groups for chosen activity type
            if len(random_course.activities[activity_type]) < 2:
                continue
            
            # make sure to avoid infinite loop if all other groups are full
            attempt = 0
            random_new_group = self.pick_activity_from_course(activity_type, random_course)

            # if the same activity is chosen as new activity or new activity is at or over capacity pick new activity again
            while random_activity == random_new_group or len(random_new_group.student_list) >= random_new_group.capacity:
                random_new_group = self.pick_activity_from_course(activity_type, random_course)
                attempt += 1
                if attempt > 10:
                    break
            
            # if after the while loop new activity still is same as conflict activity or chosen group is full continue
            if random_activity == random_new_group or len(random_new_group.student_list) >= random_new_group.capacity:
                continue

            self.timetable.swap_student_activity(random_student, random_activity, random_new_group)
            check_individual_conflicts(self.timetable)

            return self.timetable
        
        return self.timetable

    def switch_individual_student(self):
        """
        """
        for i in range(20):
            random_student = self.pick_random_student()

            random_course = random.choice(list(random_student.pers_activities.keys()))

            student_activity_list = random_student.pers_activities[random_course]
            random_activity = random.choice(student_activity_list)

            # go to next iteration of loop if chosen activity type is lecture
            if random_activity.activity_type == 'Lecture':
                continue

            activity_type = random_activity.activity_type

            # check if there are at least 2 groups for chosen activity type
            if len(random_course.activities[activity_type]) < 2:
                continue
            
            # make sure to avoid infinite loop if all other groups are full
            attempt = 0
            random_new_group = self.pick_activity_from_course(activity_type, random_course)

            # if the same activity is chosen as new activity or new activity is at or over capacity pick new activity again
            while random_activity == random_new_group or len(random_new_group.student_list) >= random_new_group.capacity:
                random_new_group = self.pick_activity_from_course(activity_type, random_course)
                attempt += 1
                if attempt > 10:
                    break
            
            # if after the while loop new activity still is same as conflict activity or chosen group is full continue
            if random_activity == random_new_group or len(random_new_group.student_list) >= random_new_group.capacity:
                continue

            self.timetable.swap_student_activity(random_student, random_activity, random_new_group)
            check_individual_conflicts(self.timetable)

            return self.timetable
        
        return self.timetable

    def add_new_activity_to_course(self):
        for i in range(10):
            conflict_student = random.choice(self.timetable.conflict_students)
            conflict_timeslot = random.choice(list(conflict_student.conflict_activities.keys()))
            conflict_activity = random.choice(conflict_student.conflict_activities[conflict_timeslot])
              
            if conflict_activity.activity_type == 'Lecture':        
                continue
            
            self.timetable.find_empty_locations()
            
            if len(self.timetable.empty_locations.keys()) > 0:
                new_activity = self.timetable.add_new_activity_to_course(conflict_activity.course, conflict_activity.activity_type)
                
            if new_activity:
                new_timeslot = random.choice(list(self.timetable.empty_locations.keys()))
                new_location = random.choice(self.timetable.empty_locations[new_timeslot])
                self.timetable.add_activity_to_timetable(self, new_activity, new_timeslot, new_location)
                self.timetable.swap_student_activity(conflict_student, conflict_activity, new_activity)
                return
        

    def apply_random_swap(self):
        """
        This function applies the random swap chosen in the random_swap function.
        """
        random_function = self.random_swap(self.timetable)
        
        if random_function == self.random_students_swap:
            swapped_timetable = self.random_students_swap()

        if random_function == self.random_activities_swap:
            swapped_timetable = self.random_activities_swap()
        
        if random_function == self.random_activity_location_swap:
            swapped_timetable = self.random_activity_location_swap()

        if random_function == self.switch_conflict_student:
            swapped_timetable = self.switch_conflict_student()

        if random_function == self.switch_individual_student:
            swapped_timetable = self.switch_individual_student()
        
        if random_function == self.add_new_activity_to_course:
            swapped_timetable = self.add_new_activity_to_course()
        
        return swapped_timetable
    
    def random_swap(self):
        """
        This function randomly chooses 1 out of 4 swaps. The 4 swaps are: switch_students,
        switch_activities_in_timetable, switch_activity_in_timetable and switch_student.
        Also if gap hour malus points are under 30, there is a 51.25% chance switch_student
        gets picked to prioritize swapping students with individual conflict when approaching the end.
        """

     
        # choose a random swap
        random_swap_function = random.choice([self.random_students_swap, 
                                            self.random_activities_swap, 
                                            self.random_activity_location_swap, 
                                            self.switch_conflict_student, 
                                            self.switch_individual_student,
                                            self.add_new_activity_to_course])
        
        return random_swap_function

    def pick_random_student(self):
        return random.choice(self.timetable.full_student_list)
    
    def pick_random_activity(self):
        return random.choice(self.timetable.activity_list)
    
    def pick_random_course(self):
        return random.choice(self.timetable.courses)

    def pick_activity_from_course(self, activity_type, course):
        return random.choice(course.activities[activity_type])
    