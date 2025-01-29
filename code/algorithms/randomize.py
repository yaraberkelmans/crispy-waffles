import random
import copy
from .malus import *


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


# TODO ff chances checken
def random_swap(timetable):
    """
    This function randomly chooses 1 out of 4 swaps. The 4 swaps are: switch_students,
    switch_activities_in_timetable, switch_activity_in_timetable and switch_conflict_student.
    Also if gap hour malus points are under 30, there is a 51.25% chance switch_conflict_student
    gets picked to prioritize swapping students with individual conflict when approaching the end.
    """

    # check if malus for gap hours is sub 30
    if check_gap_hours(timetable) < 5:

        # give 65% chance to pick switch conflict student
        if random.random() > 0.65:
            random_swap_function = switch_conflict_student
            return random_swap_function
    
    # choose a random swap
    random_swap_function = random.choice([timetable.switch_students, 
                                          timetable.switch_activities_in_timetable, 
                                          timetable.switch_activity_in_timetable, 
                                          switch_conflict_student, switch_individual_student])
    
    return random_swap_function


def random_students_swap(timetable):
    """
    This function randomly chooses a course, then chooses a random activity type
    either tutorial or lab and then chooses two different groups within this course
    and activity type to pick a student out of each of the groups and then switches them
    from group. 
    """
    random_course = random.choice(timetable.courses)

    # avoid courses containing only lectures
    while list(random_course.activities.keys()) == ['Lecture']:
        random_course = random.choice(timetable.courses)

    random_activity_type = random.choice(list(random_course.activities.keys()))

    # avoid lectures and other activities with less than 2 groups
    while random_activity_type == 'Lecture' or len(random_course.activities[random_activity_type]) < 2:
        random_activity_type = random.choice(list(random_course.activities.keys()))

    random_activity_1 = random.choice(list(random_course.activities[random_activity_type]))
    random_activity_2 = random.choice(list(random_course.activities[random_activity_type]))

    # avoids choosing same activity group
    while random_activity_1 == random_activity_2:
        random_activity_2 = random.choice(list(random_course.activities[random_activity_type]))

    random_student_1 = random.choice(random_activity_1.student_list)
    random_student_2 = random.choice(random_activity_2.student_list)

    timetable.switch_students(random_student_1, random_student_2, random_activity_1, random_activity_2)

    return timetable


def random_activities_swap(timetable):
    """
    This function chooses two random activities and then switches their timeslots
    and locations to switch them around in the timetable.
    """
    random_activity_1 = random.choice(timetable.activity_list)
    random_activity_2 = random.choice(timetable.activity_list)
    
    # if the same activities are chosen pick a new activity
    while random_activity_1 == random_activity_2:
        random_activity_2 = random.choice(timetable.activity_list)
    
    timetable.switch_activities_in_timetable(random_activity_1, random_activity_2)

    return timetable

def random_activity_location_swap(timetable):
    """
    This function randomly chooses an activity to switch to a random empty
    location.
    """
    random_activity = random.choice(timetable.activity_list)

    # refresh empty location list
    timetable.find_empty_locations()

    # choose from empty locations
    random_timeslot = random.choice(list(timetable.empty_locations.keys()))
    random_location = random.choice(list(timetable.empty_locations[random_timeslot]))
    
    # choose random activity instead of new random empty location to avoid infinite loop if all location
    # capacities are smaller then length activity student list
    while random_location.capacity < len(random_activity.student_list):
        random_activity = random.choice(timetable.activity_list)
    
    timetable.switch_activity_in_timetable(random_activity, random_timeslot, random_location)

    return timetable


def switch_conflict_student(timetable):
    """
    This function chooses a student out of all students that have conflicting activities. It
    tries to do this 20 times to prevent choosing a student that only has lectures as 
    conflicting activities (because each student following a course attends each lecture) or
    choosing a student for who all conflicting activity groups are full.
    """
    
    # make sure to stop after 20 attempts if all conflict students only have lectures 
    # or for every student every other group for conflict activity type is full
    for i in range(20):
        random_conflict_student = random.choice(timetable.conflict_students)

        random_conflict_timeslot = random.choice(list(random_conflict_student.conflict_activities.keys()))

        conflict_activity_list = random_conflict_student.conflict_activities[random_conflict_timeslot]
        random_conflict_activity = random.choice(conflict_activity_list)

        # go to next iteration of loop if chosen activity type is lecture
        if random_conflict_activity.activity_type == 'Lecture':
            continue

        conflict_course = random_conflict_activity.course
        conflict_activity_type = random_conflict_activity.activity_type

        # check if there are at least 2 groups for chosen activity type
        if len(conflict_course.activities[conflict_activity_type]) < 2:
            continue
        
        # make sure to avoid infinite loop if all other groups are full
        attempt = 0
        random_new_group = random.choice(conflict_course.activities[conflict_activity_type])

        # if the same activity is chosen as new activity or new activity is at or over capacity pick new activity again
        while random_conflict_activity == random_new_group or len(random_new_group.student_list) >= random_new_group.capacity:
            random_new_group = random.choice(conflict_course.activities[conflict_activity_type])
            attempt += 1
            if attempt > 10:
                break
        
        # if after the while loop new activity still is same as conflict activity or chosen group is full continue
        if random_conflict_activity == random_new_group or len(random_new_group.student_list) >= random_new_group.capacity:
            continue

        timetable.swap_student_activity(random_conflict_student, random_conflict_activity, random_new_group)
        check_individual_conflicts(timetable)

        return timetable
    
    return timetable

def switch_individual_student(timetable):
    """
    """
    for i in range(20):
        random_student = random.choice(timetable.full_student_list)

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
        random_new_group = random.choice(random_course.activities[activity_type])

        # if the same activity is chosen as new activity or new activity is at or over capacity pick new activity again
        while random_activity == random_new_group or len(random_new_group.student_list) >= random_new_group.capacity:
            random_new_group = random.choice(random_course.activities[activity_type])
            attempt += 1
            if attempt > 10:
                break
        
        # if after the while loop new activity still is same as conflict activity or chosen group is full continue
        if random_activity == random_new_group or len(random_new_group.student_list) >= random_new_group.capacity:
            continue

        timetable.swap_student_activity(random_student, random_activity, random_new_group)
        check_individual_conflicts(timetable)

        return timetable
    
    return timetable

def add_activity_to_course(timetable)

def apply_random_swap(timetable):
    """
    This function applies the random swap chosen in the random_swap function.
    """
    random_function = random_swap(timetable)
    
    if random_function == timetable.switch_students:
        swapped_timetable = random_students_swap(timetable)

    if random_function == timetable.switch_activities_in_timetable:
        swapped_timetable = random_activities_swap(timetable)
    
    if random_function == timetable.switch_activity_in_timetable:
        swapped_timetable = random_activity_location_swap(timetable)

    if random_function == switch_conflict_student:
        swapped_timetable = switch_conflict_student(timetable)

    if random_function == switch_individual_student:
        swapped_timetable = switch_individual_student(timetable)

    return swapped_timetable

