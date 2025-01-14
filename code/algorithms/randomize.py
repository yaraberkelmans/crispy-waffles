import random
import copy

def randomize(timetable):
    randomized_courses = random_course_assignment(timetable)
    randomized_student_couses = random_student_course_assignment(randomized_courses)
    
    return random_student_class_assignment(randomized_student_couses)

def random_course_assignment(timetable):
    """This function randomly assigns courses to a timetable until the amount of total classes has been assigned."""
    new_timetable_object = copy.deepcopy(timetable)
    new_classes_list = new_timetable_object.classes_list
    new_timetable = new_timetable_object.timetable
    classes_added = 0
    
    while classes_added < len(new_classes_list):
        random_timeslot = random.choice(list(new_timetable.keys()))
        random_classroom = random.choice(list(new_timetable[random_timeslot]))
        random_class = random.choice(list(new_classes_list))

        if new_timetable[random_timeslot][random_classroom] == None:
            new_timetable[random_timeslot][random_classroom] = random_class
            classes_added += 1
    
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
        
def random_student_class_assignment(timetable):
    new_timetable = copy.deepcopy(timetable)
    for course in new_timetable.courses:
        for activity in course.classes: 
            while len(activity.student_list) < activity.capacity:
                random_student = random.choice(new_timetable.full_student_list)
                if random_student in activity.student_list:
                    continue
                activity.student_list.append(random_student)
    return new_timetable
        