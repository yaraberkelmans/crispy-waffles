import random
import copy
from .malus import *

def randomize(timetable):
    """
    This function creates a new random timetable by random assigning courses, activities and students to timeslots and rooms.
    """
    new_timetable = copy.deepcopy(timetable)
    
    #randomized_student_courses = random_student_course_assignment(new_timetable)
    randomized_student_courses_activities = random_student_activity_assignment(new_timetable)
    randomized_timetable = random_course_assignment(randomized_student_courses_activities)
    return randomized_timetable

def random_course_assignment(timetable):
    """
    This function randomly assigns activities to timeslots and rooms in the timetable until all activities are assigned.
    """
    new_timetable = copy.copy(timetable)
    new_activities_list = copy.copy(new_timetable.activity_list)
    #print(len(new_activities_list))
    activity_count = len(new_activities_list)
    # for course in new_timetable.courses:
    #     for activity in course.activities:
    #         new_activities_list.append(activity) #this activity list is not updated, activities are stored as attr in .course_list
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
    # new_timetable = copy.deepcopy(timetable)
    new_timetable = timetable
    for course in new_timetable.courses:
        while len(course.student_list) < course.e_students:
            random_student = random.choice(new_timetable.full_student_list)
            if random_student in course.student_list:
                continue
            course.add_individual_student(random_student)
            # print('student added moi')
    return new_timetable


def random_student_activity_assignment(timetable):
    """
    This function randomly assigns students to activities within their courses,
    taking the capacity constraints of the activity into account. 
    """
    # new_timetable = copy.deepcopy(timetable)
    new_timetable = timetable

    for course in new_timetable.courses: # not your timetable
        # print('Course activities are:', course.activities)
        
        for activity_type in course.activities.keys():
            for activity in course.activities[activity_type][:-1]:
                while len(activity.student_list) < activity.initial_capacity:
                    # for student in course.student_list:
                    #     print(student)
                    valid_students = [st for st in course.student_list if st not in activity.student_list and st.check_validity(activity)]
                    if not valid_students:

                        # no more valid students, break to avoid infinite loop
                        break
                    random_student = random.choice(valid_students)
                    new_timetable.add_student_to_activity(random_student, activity)

            # print(f'Course: {course}, Activity: {activity} has {len(activity.student_list)} students.')

            # place remaining students in the last activity
            last_activity = course.activities[activity_type][-1]
            valid_students = [
                st for st in course.student_list
                if st not in last_activity.student_list and st.check_validity(last_activity)
            ]
            for student in valid_students:
                new_timetable.add_student_to_activity(student, last_activity)

        # print(f'Course: {course}, Last Activity: {last_activity} has {len(last_activity.student_list)} students.')

    return new_timetable

def random_swap(timetable):
    """
    This function randomly chooses 1 out of 4 swaps. The 4 swaps are: switch_students,
    switch_activities_in_timetable, switch_activity_in_timetable and switch_conflict_student.
    Also if gap hour malus points are under 30, there is a 70% chance switch_conflict_student
    gets picked to prioritize swapping students with individual conflict when approaching the end.
    """

    # check if malus for gap hours is sub 30
    if check_gap_hours(timetable) < 30:

        # give 60% chance to pick switch conflict student
        if random.random() > 0.4:
            random_swap_function = timetable.switch_conflict_student
            return random_swap_function
    
    # choose a random swap
    random_swap_function = random.choice([timetable.switch_students, 
                                          timetable.switch_activities_in_timetable, 
                                          timetable.switch_activity_in_timetable, 
                                          timetable.switch_conflict_student])
    
    return random_swap_function


def random_students_swap(timetable):
    """
    This function randomly chooses a course, then chooses a random activity type
    either tutorial or lab and then chooses two different groups within this course
    and activity type to pick a student out of each of the groups and then switches them
    from group. 
    """
     #print(f'The random function is {random_function}')
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

    # print(f'The chosen activity type is {random_activity_type} and the chosen activities are {random_activity_1} and {random_activity_2}')
    # print(f'The chosen students are {random_student_1} from {random_activity_1} and {random_student_2} from {random_activity_2}')
    # print(f'Student list check for activity 1: {random_activity_1.student_list}')
    # print(f'Student list check for activity 2: {random_activity_2.student_list}')

    timetable.switch_students(random_student_1, random_student_2, random_activity_1, random_activity_2)

    # if random_student_1 in random_activity_2.student_list and random_student_2 in random_activity_1.student_list:
    #     print(f'{random_student_1} is now in {random_activity_2} and {random_student_2} is now in {random_activity_1}')

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
    
    # print(f'The chosen activities and their information are {random_activity_1} Old timeslot: {random_activity_1.timeslot}, Old location{random_activity_1.location}')
    # print(f'and {random_activity_2}, Old timeslot: {random_activity_2.timeslot}, Old location{random_activity_2.location}')
    
    timetable.switch_activities_in_timetable(random_activity_1, random_activity_2)
    
    # print(f'The new location for {random_activity_1} is {random_activity_1.location} and the new timeslot is {random_activity_1.timeslot}')
    # print(f'The new location for {random_activity_2} is {random_activity_2.location} and the new timeslot is {random_activity_2.timeslot}')
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
    
    # print(f'Random activity chosen {random_activity}, old location: {random_activity.location} old timeslot: {random_activity.timeslot}')
    timetable.switch_activity_in_timetable(random_activity, random_timeslot, random_location)
    # print(f'Random activity chosen {random_activity}, new location: {random_activity.location} new timeslot: {random_activity.timeslot}')

    return timetable

def switch_conflict_student(timetable):
    """
    This function chooses a student out of students that have conflicting activities. It
    tries to do this 20 times to prevent choosing a student that only has lectures as 
    conflicting activities (because each student following a course attends each lecture) or
    choosing a student for who all conflicting activity groups are full.
    """
    
    # make sure to stop after 20 attempts if all conflict students only have lectures 
    # or for every student every other group for conflict activity type is full
    for i in range(20):
        random_conflict_student = random.choice(timetable.conflict_students)
        print(f'Chosen student is {random_conflict_student}')

        random_conflict_timeslot = random.choice(list(random_conflict_student.conflict_activities.keys()))
        print(f'Chosen timeslot is {random_conflict_timeslot}')

        conflict_activity_list = random_conflict_student.conflict_activities[random_conflict_timeslot]
        random_conflict_activity = random.choice(conflict_activity_list)
        print(random_conflict_student, random_conflict_activity, random_conflict_student.conflict_activities)
        
        # try the other activity if lecture is chosen
        # if random_conflict_activity.activity_type == 'Lecture':
        #     random_conflict_activity = random.choice(conflict_activity_list)

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
        
        print(f'\nSwitch {random_conflict_student} from {random_conflict_activity} to {random_new_group} \n')
        print(f'----------Student list for {random_new_group}-----------')
        print(random_new_group.student_list)
        print(f'----------Student list for {random_conflict_activity}-----------')
        print(random_conflict_activity.student_list)

        timetable.swap_student_activity(random_conflict_student, random_conflict_activity, random_new_group)

        print(f'\nSwitched {random_conflict_student} from {random_conflict_activity} to {random_new_group} \n')
        print(f'----------Student list for {random_new_group}-----------')
        print(random_new_group.student_list)
        print(f'----------Student list for {random_conflict_activity}-----------')
        print(random_conflict_activity.student_list)

        return timetable
    return timetable

def apply_random_swap(timetable):
    """
    This function apply the random swap chosen in the random_swap function.
    """
    random_function = random_swap(timetable)
    
    if random_function == timetable.switch_students:
        # print(f'Random function is {random_function}')
        swapped_timetable = random_students_swap(timetable)

    if random_function == timetable.switch_activities_in_timetable:
        # print(f'Random function is {random_function}')
        swapped_timetable = random_activities_swap(timetable)
    
    if random_function == timetable.switch_activity_in_timetable:
        # print(f'The random function is {random_function}')
        swapped_timetable = random_activity_location_swap(timetable)

    if random_function == timetable.switch_conflict_student:

        swapped_timetable = timetable.switch_conflict_student(timetable)

    return swapped_timetable

# old version of apply random swap which is not split up
# def apply_random_swap_old(timetable):
#     random_function = random_swap(timetable)
#     if random_function == timetable.switch_students:
#         #print(f'The random function is {random_function}')
#         random_course = random.choice(timetable.courses)

#         # avoid courses containing only lectures
#         while list(random_course.activities.keys()) == ['Lecture']:
#             random_course = random.choice(timetable.courses)

#         random_activity_type = random.choice(list(random_course.activities.keys()))

#         # avoid lectures and other activities with less than 2 groups
#         while random_activity_type == 'Lecture' or len(random_course.activities[random_activity_type]) < 2:
#             random_activity_type = random.choice(list(random_course.activities.keys()))

#         random_activity_1 = random.choice(list(random_course.activities[random_activity_type]))
#         random_activity_2 = random.choice(list(random_course.activities[random_activity_type]))

#         # avoids choosing same activity group
#         while random_activity_1 == random_activity_2:
#             random_activity_2 = random.choice(list(random_course.activities[random_activity_type]))

#         random_student_1 = random.choice(random_activity_1.student_list)
#         random_student_2 = random.choice(random_activity_2.student_list)

#         # print(f'The chosen activity type is {random_activity_type} and the chosen activities are {random_activity_1} and {random_activity_2}')
#         # print(f'The chosen students are {random_student_1} from {random_activity_1} and {random_student_2} from {random_activity_2}')
#         # print(f'Student list check for activity 1: {random_activity_1.student_list}')
#         # print(f'Student list check for activity 2: {random_activity_2.student_list}')

#         timetable.switch_students(random_student_1, random_student_2, random_activity_1, random_activity_2)

#         # if random_student_1 in random_activity_2.student_list and random_student_2 in random_activity_1.student_list:
#         #     print(f'{random_student_1} is now in {random_activity_2} and {random_student_2} is now in {random_activity_1}')

#     if random_function == timetable.switch_activities_in_timetable:
#         #print(f'Random function is {random_function}')
        
#         random_activity_1 = random.choice(timetable.activity_list)
#         random_activity_2 = random.choice(timetable.activity_list)
        
#         while random_activity_1 == random_activity_2:
#             random_activity_2 = random.choice(timetable.activity_list)
        
#         # print(f'The chosen activities and their information are {random_activity_1} Old timeslot: {random_activity_1.timeslot}, Old location{random_activity_1.location}')
#         # print(f'and {random_activity_2}, Old timeslot: {random_activity_2.timeslot}, Old location{random_activity_2.location}')
        
#         timetable.switch_activities_in_timetable(random_activity_1, random_activity_2)
        
#         # print(f'The new location for {random_activity_1} is {random_activity_1.location} and the new timeslot is {random_activity_1.timeslot}')
#         # print(f'The new location for {random_activity_2} is {random_activity_2.location} and the new timeslot is {random_activity_2.timeslot}')

#     #if random_function == timetable.swap_student_activity:

#     if random_function == timetable.switch_activity_in_timetable:
#         #print(f'The random function is {random_function}')
#         random_activity = random.choice(timetable.activity_list)
#         timetable.find_empty_locations()
#         random_timeslot = random.choice(list(timetable.empty_locations.keys()))
#         random_location = random.choice(list(timetable.empty_locations[random_timeslot]))
        
#         # choose random activity instead of new random empty location to avoid infinite loop if all location
#         # capacities are smaller then length activity student list
#         while random_location.capacity < len(random_activity.student_list):
#             random_activity = random.choice(timetable.activity_list)
#         #print(f'Random activity chosen {random_activity}, old location: {random_activity.location} old timeslot: {random_activity.timeslot}')
#         timetable.switch_activity_in_timetable(random_activity, random_timeslot, random_location)
#         #print(f'Random activity chosen {random_activity}, new location: {random_activity.location} new timeslot: {random_activity.timeslot}')

#     return timetable