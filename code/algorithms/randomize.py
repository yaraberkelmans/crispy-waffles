import random
import copy

def random_course_assignment(timetable):
    """This function randomly assigns courses to a timetable until the amount of total classes has been assigned."""
    new_classes_list = copy.deepcopy(timetable.classes_list)
    new_timetable = copy.deepcopy(timetable.timetable)
    classes_added = 0
    
    while classes_added < len(new_classes_list):
        random_timeslot = random.choice(list(new_timetable.keys()))
        random_classroom = random.choice(list(new_timetable[random_timeslot]))
        random_class = random.choice(list(new_classes_list))

        if new_timetable[random_timeslot][random_classroom] == None:
            new_timetable[random_timeslot][random_classroom] = random_class
            classes_added += 1
    
    return new_timetable

def random_student_assignment(timetable, student_list):
    pass
        