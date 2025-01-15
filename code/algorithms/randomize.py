import random
import copy

def randomize(timetable):
    randomized_courses = random_course_assignment(timetable)
    randomized_student_couses = random_student_course_assignment(randomized_courses)
    
    return random_student_activity_assignment(randomized_student_couses)

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
    return new_timetable
        
def random_student_activity_assignment(timetable):
    new_timetable = copy.deepcopy(timetable)
    for course in new_timetable.courses:
        for activity in course.activities: 
            while len(activity.student_list) < activity.capacity:
                random_student = random.choice(course.student_list)
                if random_student in activity.student_list:
                    continue
                activity.student_list.append(random_student)
                
    return new_timetable
        