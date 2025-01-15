import random
import copy


def randomize(timetable):
    randomized_courses = random_course_assignment(timetable)
    randomized_student_courses = random_student_course_assignment(randomized_courses)
    
    return random_student_activity_assignment(randomized_student_courses)

def random_course_assignment(timetable):
    """This function randomly assigns courses to a timetable until the amount of total activities has been assigned."""
    new_timetable_object = copy.deepcopy(timetable)
    new_activities_list = new_timetable_object.activity_list
    new_timetable = new_timetable_object.timetable
    activities_added = 0
    
    while activities_added < len(new_activities_list):
        random_timeslot = random.choice(list(new_timetable.keys()))
        random_room = random.choice(list(new_timetable[random_timeslot]))
        random_activity = random.choice(list(new_activities_list))

        if new_timetable[random_timeslot][random_room] == None:
            new_timetable[random_timeslot][random_room] = random_activity
            activities_added += 1
    
    return new_timetable_object

def random_student_course_assignment(timetable):
    new_timetable = copy.deepcopy(timetable)
    for course in new_timetable.courses:
        while len(course.student_list) < course.e_students:
            random_student = random.choice(new_timetable.full_student_list)
            if random_student in course.student_list:
                continue
            course.add_individual_student(random_student)
            # print('student added moi')
    return new_timetable

def random_student_activity_assignment(timetable):
    new_timetable = copy.deepcopy(timetable)

    for course in new_timetable.courses:
        print('Course activities are:', course.activities)
        
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
    
    return new_timetable