import random
import copy


def randomize(timetable):
    new_timetable = copy.deepcopy(timetable)
    randomized_courses = random_course_assignment(new_timetable)
    randomized_student_courses = random_student_course_assignment(randomized_courses)
    randomized_student_courses_activities = random_student_activity_assignment(randomized_student_courses)
    
    return randomized_student_courses_activities

def random_course_assignment(timetable):
    """This function randomly assigns courses to a timetable until the amount of total activities has been assigned."""
    # new_timetable = copy.deepcopy(timetable)
    new_timetable = timetable
    new_activities_list = new_timetable.activity_list
    new_timetable_dict = new_timetable.timetable
    activities_added = 0
    new_activities_list_choices= copy.deepcopy(new_activities_list)
    while activities_added < len(new_activities_list):
        random_timeslot = random.choice(list(new_timetable_dict.keys()))
        random_room = random.choice(list(new_timetable_dict[random_timeslot]))
        random_activity = random.choice(list(new_activities_list_choices))
        

        if new_timetable_dict[random_timeslot][random_room] is None:
            new_timetable_dict[random_timeslot][random_room] = random_activity
            random_activity.timeslot = random_timeslot
            random_activity.location = random_room
            new_activities_list_choices.remove(random_activity)
            
            activities_added += 1
    
    return new_timetable

def random_student_course_assignment(timetable):
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
    # new_timetable = copy.deepcopy(timetable)
    new_timetable = timetable

    for course in new_timetable.courses:
        # print('Course activities are:', course.activities)
        
        # place students into all but the last activity
        for activity in course.activities[:-1]:
            while len(activity.student_list) < activity.capacity:
                valid_students = [
                    st for st in course.student_list
                    if st not in activity.student_list and st.check_validity(activity)
                ]
                if not valid_students:

                    # no more valid students, break to avoid infinite loop
                    break
                random_student = random.choice(valid_students)
                new_timetable.add_student_to_activity(random_student, activity)
            
            print(f'Course: {course}, Activity: {activity} has {len(activity.student_list)} students.')

        # place remaining students in the last activity
        last_activity = course.activities[-1]
        valid_students = [
            st for st in course.student_list
            if st not in last_activity.student_list and st.check_validity(last_activity)
        ]
        for student in valid_students:
            new_timetable.add_student_to_activity(student, last_activity)

        print(f'Course: {course}, Last Activity: {last_activity} has {len(last_activity.student_list)} students.')
    
    # het gaat hier fout, volgensmij worden de activities in de timeslot niet geupdate.
    for timeslot, rooms in new_timetable.timetable.items():
        for room, activity in rooms.items():
            if activity:
                print(f"Course: {activity.course} Activity {activity.name} in {room} during {timeslot}: {len(activity.student_list)} students.")
                print(f"Students: {[student.name for student in activity.student_list]}")
    
    return new_timetable